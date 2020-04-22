"""
Content : Translator (Mask to CIDR and Wildcard Mask)
Using : Python

Author : Arthur
Date : March 2020
Context : Personal
"""


# --- --- --- Imports --- --- --- #
import re


# --- --- --- Constant --- --- --- #
IP_MASK_REGEX = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"


# --- --- --- Program Loop : Start --- --- --- #
loop = ""
while loop != "exit":
    print("Welcome : This is Mask to CIDR convertor !")

    # --- --- --- Input : Mask --- --- --- #
    # Input -> Verification then Decimal Mask List -> lDecMask
    vMask = True
    while vMask:
        sDecMask = input("Enter a Mask : ")
        print()
        if bool(re.match(IP_MASK_REGEX, sDecMask)):
            lDecMask = sDecMask.split('.')
            check = False
            for i in range(4):
                if lDecMask[i] != '255' and lDecMask[i] != '254' and lDecMask[i] != '252' and lDecMask[i] != '248' and lDecMask[i] != '240' and lDecMask[i] != '224' and lDecMask[i] != '192' and lDecMask[i] != '128' and lDecMask[i] != '0':
                    check = True
                    print("Warning : " + lDecMask[i] + " is not a valid byte.")
                elif i != 3 and lDecMask[i] != '255' and lDecMask[i+1] != '0':
                    check = True
                    print(
                        "Warning : This is not a valid Mask all bits must be left contiguous.")
            if check:
                vMask = True
            else:
                vMask = False
        else:
            vMask = True
            print("Warning : This is not a valid Mask.")

    # --- --- --- Calculation : WildCard --- --- --- #
    # lDecMask -> Decimal Mask List to Decimal WildaCard Mask String -> sDecWMask
    sDecWMask = ""
    for i in range(3):
        sDecWMask = sDecWMask + str(255 - int(lDecMask[i]))
        sDecWMask = sDecWMask + '.'
    sDecWMask = sDecWMask + str(255 - int(lDecMask[i+1]))

    # --- --- --- Calculation : CIDR --- --- --- #
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

    # iCIDR -> CIDR Integer to CIDR String -> sCIDR
    sCIDR = "/" + str(iCIDR)

    # --- --- --- Calculation : Nbr of IPs --- --- --- #
    # iCIDR -> CIDR Integer to Nbr of IPs String -> nbIP
    nbIP = str(2**(32-iCIDR))

    # --- --- --- Calculation : Nbr of usable IPs --- --- --- #
    # iCIDR -> CIDR Integer to Nbr of usable IPs String -> nbUsableIP
    nbUsableIP = str(2**(32-iCIDR) - 2)
    if nbUsableIP < '1':
        nbUsableIP = '1'

    # --- --- --- Calculation : Nbr of SubNets --- --- --- #
    # iCIDR -> CIDR Integer to Nbr of SubNets String -> nbSubNet
    nbSubNet = str(2**(32-iCIDR-2))
    if nbSubNet < '1':
        nbSubNet = '1'

    # --- --- --- Program Loop : Outputs --- --- --- #
    print("CIDR : " + sCIDR)
    print("Wildcard Mask : " + sDecWMask)
    print("Binary Mask : " + sBinMask)
    print()
    print("Number of IPs : " + nbIP)
    print("Number of usable IPs : " + nbUsableIP)
    print()
    print("Number of SubNets : " + nbSubNet)
    print()
    print()

    # --- --- --- Program Loop : Exit or Continue --- --- --- #
    loop = input("If you want to continue press Enter else enter \"exit\" : ")
    print()
