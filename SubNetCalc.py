"""
Content : SubNet Calculator
Using : Python

Author : Arthur
Date : March 2020
Context : Personal
"""


# --- --- --- Imports --- --- --- #
import re


# --- --- --- Constant --- --- --- #
IP_MASK_REGEX = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"
CIDR_REGEX = r"^[0-9]{1,2}$"


# --- --- --- Program Loop : Start --- --- --- #
loop = ""
while loop != "exit":
    print("Welcome : This is SubNet Calculator !")

    # --- --- --- Input : IP --- --- --- #
    # input -> Verification then Decimal IP List -> lDecIP
    vIP = True
    while vIP:
        sDecIP = input("Enter your IP : ")
        print()
        if bool(re.match(IP_MASK_REGEX, sDecIP)):
            lDecIP = sDecIP.split('.')
            isNotMask = False
            for i in range(4):
                if int(lDecIP[i]) < 0 or int(lDecIP[i]) > 255:
                    isNotMask = True
                    print("Warning : " + lDecIP[i] + " is not a valid byte.")
            if isNotMask:
                vIP = True
            else:
                vIP = False
        else:
            vIP = True
            print("Warning : This is not a valid IP.")

    # --- --- --- Input : Mask or CIDR --- --- --- #
    # input -> Verification then Decimal Mask or CIDR -> lDecMask or bCIDR
    vMask = True
    while vMask:
        sMask = input("Enter your Mask or CIDR (without the \'/\') : ")
        print()
        if bool(re.match(IP_MASK_REGEX, sMask)):
            isNotMask = False
            lDecMask = sMask.split('.')
            for i in range(4):
                if lDecMask[i] != '255' and lDecMask[i] != '254' and lDecMask[i] != '252' and lDecMask[i] != '248' and lDecMask[i] != '240' and lDecMask[i] != '224' and lDecMask[i] != '192' and lDecMask[i] != '128' and lDecMask[i] != '0':
                    isNotMask = True
                    print("Warning : " + lDecMask[i] + " is not a valid byte.")
                elif i != 3 and lDecMask[i] != '255' and lDecMask[i+1] != '0':
                    isNotMask = True
                    print(
                        "Warning : This is not a valid Mask all bits must be left contiguous.")
            if isNotMask:
                vMask = True
            else:
                vMask = False

        elif bool(re.match(CIDR_REGEX, sMask)):
            isNotMask = True
            try:
                bCIDR = int(sMask)
            except:
                bCIDR = -1
            if bCIDR < 0 or bCIDR > 32:
                vMask = True
                print("Warning : CIDR must be a number between 0 and 32.")
            else:
                vMask = False
        else:
            vMask = True
            print("Warning : This is not a valid Mask or CIDR.")

    # --- --- --- Calculation : CIDR (if lDecMask) --- --- --- #
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

        # lBinMask -> Binary Mask List to CIDR Integer -> bCIDR
        iCIDR = 0
        for i in range(len(lBinMask)):
            if lBinMask[i] == '1':
                iCIDR = iCIDR + 1

    # --- --- --- Calculation : Nbr of Available IPs --- --- --- #
    # bCIDR -> CIDR Integer to Nbr of usable IPs String -> nbAvailableIP
    nbAvailableIP = str(2**(32 - bCIDR) - 2)
    if nbAvailableIP < '1':
        nbAvailableIP = '1'

    # --- --- --- Calculation : Nbr Max of SubNets --- --- --- #
    # bCIDR -> CIDR Integer to Nbr of SubNets String -> nbMaxSubNet
    nbMaxSubNet = str(2**(32-bCIDR-2))
    if nbMaxSubNet < '1':
        nbMaxSubNet = '1'

    # --- --- --- Input : Nbr of SubNets --- --- --- #
    # input -> Verification then Nbr of SubNets Integer -> nbSubNets
    vSubNets = True
    while vSubNets:
        nbSubNets = input(
            "Enter the number of SubNets you need (max " + nbMaxSubNet + "): ")
        print()
        try:
            nbSubNets = int(nbSubNets)
        except:
            nbSubNets = -1
        if nbSubNets <= 0 or nbSubNets > int(nbMaxSubNet):
            vSubNets = True
            print("Warning : You entered an invalid number (you have to enter a number > 0 and <= " + nbMaxSubNet + ").")
        else:
            vSubNets = False

    # --- --- --- Input : Nbr of Users per SubNet --- --- --- #
    # input -> Verification then Nbr of Users per SubNet Integer -> nbUsers
    if nbSubNets == 1:
        print("Enter the number of users you need for your SubNet. ")
    else:
        print("Enter the number of users in descending order for your " +
              str(nbSubNets) + " SubNets.")

    # --- --- --- Subnet Loop : Start --- --- --- #
    for nbSubNet in range(nbSubNets):
        # --- --- --- Input : Nbr of Users for the SubNet --- --- --- #
        # input -> Verification then Nbr of Users -> nbUsers.append(users)
        vNbUsers = True
        while vNbUsers:
            nbUsers = input("Enter the number of users you need for SubNet " +
                            str(nbSubNet + 1) + " (" + nbAvailableIP + " IPs availabes): ")
            print()
            try:
                nbUsers = int(nbUsers)
                vNbUsers = False
            except:
                nbUsers = -1
            if nbUsers <= 0 or nbUsers > int(nbAvailableIP):
                vNbUsers = True
                print(
                    "Warning : You entered an invalid number (you have to enter numbers between > 0 and <= " + nbAvailableIP + ").")
            elif nbSubNet != 0 and nbUsers > lastBbUsers:
                vNbUsers = True
                print(
                    "Warning : You must enter numbers of users in descending order (last was " + str(lastBbUsers) + " users).")
            else:
                lastBbUsers = nbUsers

        # --- --- --- Calculation : CIDR for the SubNet --- --- --- #
        # nbUsers[nbSubNet] -> Nbr users needed to CIDR -> iCIDR
        iCIDR = 32
        while (2**(32-iCIDR) - 2) < int(nbUsers):
            iCIDR = iCIDR - 1

        # --- --- --- Calculation : Nbr of IPs for the SubNet --- --- --- #
        # iCIDR -> CIDR Integer to Nbr of IPs String -> nbIP
        nbIP = str(2**(32-iCIDR))

        # --- --- --- Calculation : Nbr of usable IPs --- --- --- #
        # iCIDR -> CIDR Integer to Nbr of usable IPs String -> nbUsableIP
        nbUsableIP = str(2**(32-iCIDR) - 2)
        if nbUsableIP < '1':
            nbUsableIP = '1'

        # --- --- --- Calculation : Mask --- --- --- #
        # iCIDR -> CIDR Integer to Binary Mask List -> lBinMask
        lBinMask = []
        for i in range(32):
            if i < iCIDR:
                if i % 8 == 0 and i != 0:
                    lBinMask.append('.')
                lBinMask.append('1')
            else:
                if i % 8 == 0 and i != 0:
                    lBinMask.append('.')
                lBinMask.append('0')

        # lBinMask -> Binary Mask List to Decimal Mask String -> sDecMask
        sDecMask = ""
        octet = 0
        p = 7
        for i in range(35):
            if lBinMask[i] == '1':
                octet = octet + 2**p
                p = p - 1
            elif lBinMask[i] == '0':
                octet = octet + 0
                p = p - 1
            else:
                sDecMask = sDecMask + '.'
            if p < 0:
                sDecMask = sDecMask + str(octet)
                octet = 0
                p = 7

        # --- --- --- Calculation : Network and Broadcast Address --- --- --- #
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
                octet = octet + 0
                p = p - 1
            elif lBinBroad[i] == '.':
                sDecBroad = sDecBroad + '.'
            if p < 0:
                sDecBroad = sDecBroad + str(octet)
                octet = 0
                p = 7

        # --- --- --- Subnet Loop : Outputs --- --- --- #
        print("--- --- --- SubNet " + str(nbSubNet + 1) + " --- --- ---")
        print("Network Address : " + sDecNet)
        print("Broadcast Address : " + sDecBroad)
        print("Mask : " + sDecMask)
        print("CIDR : /" + str(iCIDR))
        print()
        print("Number of IPs : " + nbIP)
        print("Number of usable IPs : " + nbUsableIP)
        print()
        print()

        # --- --- --- Subnet Loop : Update  --- --- --- #
        # iCIDR -> CIDR Integer to Nbr of IPs used Integer -> nbUsedIP
        nbUsedIP = str(2**(32-iCIDR))

        # nbUsedIP + nbAvailableIP -> Update and Verification Nbr of Available IPs -> nbAvailableIP
        nbAvailableIP = str(int(nbAvailableIP) + 2 - int(nbUsedIP))
        if int(nbAvailableIP) <= 0 and nbSubNets - (nbSubNet + 1) == 1:
            print("Warning : You used all available IPs. You can't create your " +
                  str(nbSubNets - (nbSubNet + 1)) + " SubNet remaining.")
            print("If you want to create it, please try with others parameters.")
            print()
            break
        elif int(nbAvailableIP) <= 0 and nbSubNets - (nbSubNet + 1) > 1:
            print("Warning : You used all available IPs. You can't create your " +
                  str(nbSubNets - (nbSubNet + 1)) + " SubNets remaining.")
            print("If you want to create them, please try with others parameters.")
            print()
            break

        # lDecIP -> Update and Verification next IP -> lDecIP
        lDecIP = sDecBroad.split('.')
        lDecIP[3] = str(int(lDecIP[3]) + 1)
        if int(lDecIP[3]) > 255:
            lDecIP[2] = str(int(lDecIP[2]) + 1)
            lDecIP[3] = '0'
            if int(lDecIP[2]) > 255:
                lDecIP[1] = str(int(lDecIP[1]) + 1)
                lDecIP[2] = '0'
                if int(lDecIP[1]) > 255:
                    lDecIP[0] = str(int(lDecIP[0]) + 1)
                    lDecIP[1] = '0'
                    if int(lDecIP[0]) > 255:
                        print(
                            "Error : It's seems that there is a problem. Please report it to Cytzen.")
                        break

    # --- --- --- Program Loop : Exit or Continue --- --- --- #
    loop = input("If you want to continue press Enter else enter \"exit\" : ")
    print()
