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


# --- --- --- Loop --- --- --- #
loop = ""
while loop != "exit":
    print("Welcome : This is SubNet Calculator !")

    # --- --- --- Input : IP --- --- --- #
    # lDecIP
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
    # lDecMask
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

    # --- --- --- CIDR if Input is Mask --- --- --- #
    if isNotMask == False:
        # sBinMask
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

        # bBinMask
        # bCIDR
        bBinMask = list(sBinMask)
        bCIDR = 0
        for i in range(len(bBinMask)):
            if bBinMask[i] == '1':
                bCIDR = bCIDR + 1

    # --- --- --- Nbr Max of IPs --- --- --- #
    # nbMaxIp
    nbMaxIp = str(2**(32-bCIDR))
    if nbMaxIp == '1':
        nbMaxUsable = '1'
    else:
        nbMaxUsable = str(2**(32-bCIDR) - 2)

    # --- --- --- Nbr Max of SubNets --- --- --- #
    # nbMaxSubNet
    nbMaxSubNet = str(2**(32-bCIDR-2))
    if nbMaxSubNet < '1':
        nbMaxSubNet = '1'

    # --- --- --- Input : Nbr of SubNets --- --- --- #
    # nbSubNets
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
    if vSubNets == 1:
        nbUsers = input(
            "Enter the number of users you need for your SubNet (max " + nbMaxUsable + " users) : ")
    else:
        print("Enter the number of users in descending order for your " +
              str(nbSubNets) + " SubNets.")

    # --- --- --- Variables Initialization  --- --- --- #
    oDecRes = []
    oDecBroad = []
    oDecMask = []
    oCIDR = []
    oNbMaxIp = []
    oNbUsable = []
    nbUsers = []
    nbAvailableIP = nbMaxUsable

    # --- --- --- Loop Subnets Creation --- --- --- #
    for nbSubNet in range(nbSubNets):
        vNbUsers = True
        while vNbUsers:
            users = input("Enter the number of users you need for SubNet " +
                          str(nbSubNet + 1) + " (" + nbAvailableIP + " IPs availabes): ")
            print()
            try:
                users = int(users)
                vNbUsers = False
            except:
                users = -1
            if users <= 0 or users > int(nbAvailableIP):
                vNbUsers = True
                print(
                    "Warning : You entered an invalid number (you have to enter numbers between > 0 and <= " + nbAvailableIP + ").")
            elif nbSubNet != 0 and users > nbUsers[nbSubNet-1]:
                vNbUsers = True
                print(
                    "Warning : You must enter numbers of users in descending order (last was " + str(nbUsers[nbSubNet-1]) + " users).")
            else:
                nbUsers.append(users)

        # --- --- --- Subnet : CIDR --- --- --- #
        # iCIDR
        iCIDR = 32
        while (2**(32-iCIDR) - 2) < int(nbUsers[nbSubNet]):
            iCIDR = iCIDR - 1

        # --- --- --- Subnet : Nbr of IPs --- --- --- #
        # nbMaxIp
        nbMaxIp = str(2**(32-iCIDR))
        if nbMaxIp == '1':
            nbUsable = '1'
        else:
            nbUsable = str(2**(32-iCIDR) - 2)

        # --- --- --- Subnet : Mask --- --- --- #
        # lBinMask
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

        # sDecMask
        sDecMask = ""
        octet = 0
        wOctet = 0
        p = 7
        for i in range(35):
            if lBinMask[i] == '1':
                octet = octet + 2**p
                wOctet = wOctet + 0
                p = p - 1
            elif lBinMask[i] == '0':
                octet = octet + 0
                wOctet = wOctet + 2**p
                p = p - 1
            else:
                sDecMask = sDecMask + '.'
            if p < 0:
                sDecMask = sDecMask + str(octet)
                octet = 0
                wOctet = 0
                p = 7

        # --- --- --- Subnet : Network and Broadcast Address --- --- --- #
        # sBinIP
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

        # lBinIP
        lBinIP = list(sBinIP)

        # lBinRes
        # lBinBroad
        lBinRes = []
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
                lBinRes.append('.')
                lBinBroad.append('.')
            else:
                if i < aCIDR and aCIDR != 0:
                    lBinRes.append(lBinIP[i])
                    lBinBroad.append(lBinIP[i])
                else:
                    lBinRes.append('0')
                    lBinBroad.append('1')

        # sDecRes
        sDecRes = ""
        octet = 0
        p = 7
        for i in range(35):
            if lBinRes[i] == '1':
                octet = octet + 2**p
                p = p - 1
            elif lBinRes[i] == '0':
                octet = octet + 0
                p = p - 1
            elif lBinRes[i] == '.':
                sDecRes = sDecRes + '.'
            if p < 0:
                sDecRes = sDecRes + str(octet)
                octet = 0
                p = 7

        # sDecBroad
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

        # --- --- --- Subnet : Save for Output --- --- --- #
        oDecRes.append(sDecRes)
        oDecBroad.append(sDecBroad)
        oDecMask.append(sDecMask)
        oCIDR.append(iCIDR)
        oNbMaxIp.append(nbMaxIp)
        oNbUsable.append(nbUsable)

        # --- --- --- Update --- --- --- #
        # nbUsedIP
        nbUsedIP = str(2**(32-iCIDR))
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
            

        # lDecIP
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
                            "Error : It's seems that there is a problem. Please report it on the Github.")
                        break
    
    # --- --- --- Subnet : Outputs --- --- --- #
    for nbSubNet in range (len(oDecRes)):
        print("--- --- --- SubNet " + str(nbSubNet + 1) + " --- --- ---")
        print("Network Address : " + oDecRes[nbSubNet])
        print("Broadcast Address : " + oDecBroad[nbSubNet])
        print("Mask : " + oDecMask[nbSubNet])
        print("CIDR : /" + str(oCIDR[nbSubNet]))
        print()
        print("Number of IPs : " + oNbMaxIp[nbSubNet])
        print("Number of usable IPs : " + oNbUsable[nbSubNet])
        print()
        print()

    # --- --- --- Exit or Continue --- --- --- #
    loop = input("If you want to continue press Enter else enter \"exit\" : ")
    print()
