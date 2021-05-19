"""
Content: IP Range Calculator
Using: Python

Author: Arthur
Date: March 2020
Context: Personal
"""

# --- --- --- Imports --- --- --- #
import re


# --- --- --- Constant --- --- --- #
IP_MASK_REGEX = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"
CIDR_REGEX = r"^[0-9]{1,2}$"


# --- --- --- Program Loop: Start --- --- --- #
loop = ""
while loop != "exit":
    print("Welcome: This is IP Range Calculator!")

    # --- --- --- Input: IP --- --- --- #
    # input -> Verification then Decimal IP List -> lDecIP
    vIP = True
    while vIP:
        sDecIP = input("Enter an IP: ")
        print()
        if bool(re.match(IP_MASK_REGEX, sDecIP)):
            lDecIP = sDecIP.split('.')
            isNotMask = False
            for i in range(4):
                if int(lDecIP[i]) < 0 or int(lDecIP[i]) > 255:
                    isNotMask = True
                    print("Warning: " + lDecIP[i] + " is not a valid byte.")
            if isNotMask:
                vIP = True
            else:
                vIP = False
        else:
            vIP = True
            print("Warning: This is not a valid IP.")

    # --- --- --- Input: Mask or CIDR --- --- --- #
    # input -> Verification then Decimal Mask or CIDR -> lDecMask or iCIDR
    vMask = True
    while vMask:
        sMask = input("Enter a Mask or a CIDR (without the \'/\'): ")
        print()
        if bool(re.match(IP_MASK_REGEX, sMask)):
            isNotMask = False
            lDecMask = sMask.split('.')
            for i in range(4):
                if lDecMask[i] != '255' and lDecMask[i] != '254' and lDecMask[i] != '252' and lDecMask[i] != '248' and lDecMask[i] != '240' and lDecMask[i] != '224' and lDecMask[i] != '192' and lDecMask[i] != '128' and lDecMask[i] != '0':
                    isNotMask = True
                    print("Warning: " + lDecMask[i] + " is not a valid byte.")
                elif i != 3 and lDecMask[i] != '255' and lDecMask[i+1] != '0':
                    isNotMask = True
                    print(
                        "Warning: This is not a valid Mask all bits must be left contiguous.")
            if isNotMask:
                vMask = True
            else:
                vMask = False

        elif bool(re.match(CIDR_REGEX, sMask)):
            isNotMask = True
            try:
                iCIDR = int(sMask)
            except:
                iCIDR = -1
            if iCIDR < 0 or iCIDR > 32:
                vMask = True
                print("Warning: CIDR must be a number between 0 and 32.")
            else:
                vMask = False
        else:
            vMask = True
            print("Warning: This is not a valid Mask or CIDR.")

    # --- --- --- Calculation: CIDR (if lDecMask) --- --- --- #
    if isNotMask == False:
        # lDecMask -> Decimal Mask List to Binary Mask String -> sBinMask
        sBinMask = ""
        for i in range(3):
            if lDecMask[i] != '0':
                sBinMask = sBinMask + str("{0:b}".format(int(lDecMask[i])))
                sBinMask = sBinMask + '.'
            else:
                sBinMask = sBinMask + "00000000"
                sBinMask = sBinMask + '.'
        if lDecMask[i+1] != '0':
            sBinMask = sBinMask + str("{0:b}".format(int(lDecMask[i+1])))
        else:
            sBinMask = sBinMask + "00000000"

        # sBinMask -> Binary Mask String to Binary Mask List -> lBinMask
        lBinMask = list(sBinMask)

        # lBinMask -> Binary Mask List to CIDR Integer -> iCIDR
        iCIDR = 0
        for i in range(len(lBinMask)):
            if lBinMask[i] == '1':
                iCIDR = iCIDR + 1

    # --- --- --- Calculation: Nbr of IPs --- --- --- #
    # iCIDR -> CIDR Integer to Nbr of IPs String -> nbIP
    nbIP = str(2**(32-iCIDR))

    # --- --- --- Calculation: Nbr of usable IPs --- --- --- #
    # iCIDR -> CIDR Integer to Nbr of usable IPs String -> nbUsableIP
    nbUsableIP = str(2**(32-iCIDR) - 2)
    if nbUsableIP < '1':
        nbUsableIP = '1'

    # --- --- --- Calculation: Network and Broadcast Address --- --- --- #
    # lDecIP -> Decimal IP List to Binary IP String -> sBinIP
    sBinIP = ""
    for i in range(3):
        if lDecIP[i] != '0':
            if len("{0:b}".format(int(lDecIP[i]))) < 8:
                for j in range(8 - len("{0:b}".format(int(lDecIP[i])))):
                    sBinIP = sBinIP + '0'
                sBinIP = sBinIP + str("{0:b}".format(int(lDecIP[i])))
                sBinIP = sBinIP + '.'
            else:
                sBinIP = sBinIP + str("{0:b}".format(int(lDecIP[i])))
                sBinIP = sBinIP + '.'
        else:
            sBinIP = sBinIP + "00000000"
            sBinIP = sBinIP + '.'
    if lDecIP[i+1] != '0':
        if len("{0:b}".format(int(lDecIP[i+1]))) < 8:
            for j in range(8 - len("{0:b}".format(int(lDecIP[i+1])))):
                sBinIP = sBinIP + '0'
            sBinIP = sBinIP + str("{0:b}".format(int(lDecIP[i+1])))
        else:
            sBinIP = sBinIP + str("{0:b}".format(int(lDecIP[i+1])))
    else:
        sBinIP = sBinIP + "00000000"

    # sBinIP -> Binary IP String to Binary IP List -> lBinIP
    lBinIP = list(sBinIP)

    # lBinIP + iCIDR -> Binary IP List + CIDR to Binary Network Address List -> lBinNet
    # lBinIP + iCIDR -> Binary IP List + CIDR to Binary Broadcast Address List -> lBinBroad
    lBinNet = []
    lBinBroad = []
    if iCIDR > 24:
        aCIDR = iCIDR + 3
    elif iCIDR > 16:
        aCIDR = iCIDR + 2
    elif iCIDR > 8:
        aCIDR = iCIDR + 1
    else:
        aCIDR = iCIDR

    for i in range(35):
        if lBinIP[i] == '.':
            lBinNet.append('.')
            lBinBroad.append('.')
        else:
            if i < aCIDR and aCIDR != 0:
                lBinNet.append(lBinIP[i])
                lBinBroad.append(lBinIP[i])
            else:
                lBinNet.append('0')
                lBinBroad.append('1')

    # lBinNet -> Binary Network Address List to Decimal Network Address String -> sDecNet
    sDecNet = ""
    octet = 0
    p = 7
    for i in range(35):
        if lBinNet[i] == '1':
            octet = octet + 2**p
            p = p - 1
        elif lBinNet[i] == '0':
            octet = octet + 0
            p = p - 1
        elif lBinNet[i] == '.':
            sDecNet = sDecNet + '.'
        if p < 0:
            sDecNet = sDecNet + str(octet)
            octet = 0
            p = 7

    # lBinBroad -> Binary Broadcast Address List to Decimal Broadcast Address String -> sDecBroad
    sDecBroad = ""
    octet = 0
    p = 7
    for i in range(35):
        if lBinBroad[i] == '1':
            octet = octet + 2**p
            p = p - 1
        elif lBinBroad[i] == '0':
            p = p - 1
        elif lBinBroad[i] == '.':
            sDecBroad = sDecBroad + '.'
        if p < 0:
            sDecBroad = sDecBroad + str(octet)
            octet = 0
            p = 7

    # --- --- --- Program Loop: Outputs --- --- --- #
    print("Network Address: " + sDecNet)
    print("Broadcast Address: " + sDecBroad)
    print()
    print("Number of IPs: " + nbIP)
    print("Number of usable IPs: " + nbUsableIP)
    print()
    print()

    # --- --- --- Program Loop: Exit or Continue --- --- --- #
    loop = input("If you want to continue press Enter else enter \"exit\": ")
    print()
