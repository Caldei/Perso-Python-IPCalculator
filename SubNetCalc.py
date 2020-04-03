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


# TEST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
sDecIP = "250.168.0.0"
sDecMask = "255.255.255.0"

# --- --- --- Loop --- --- --- #
loop = ""
while loop != "exit":
    print("Welcome : This is SubNet Calculator !")
    # --- --- --- Inputs --- --- --- #
    # lDecIP
    vIP = True
    while vIP:
        #sDecIP = input("Enter an IP : ")
        print("")
        if bool(re.match(IP_MASK_REGEX, sDecIP)):
            lDecIP = sDecIP.split('.')
            check = False
            for i in range(4):
                if int(lDecIP[i]) < 0 or int(lDecIP[i]) > 255:
                    check = True
                    print("Warning : " + lDecIP[i] + " is not a valid byte.")
            if check:
                vIP = True
            else:
                vIP = False
        else:
            vIP = True
            print("Warning : This is not a valid IP.")

    # nbSubNets
    vSubNets = True
    while vSubNets:
        nbSubNets = input("Enter the number of SubNets needed (max 10): ")
        print("")
        try:
            nbSubNets = int(nbSubNets)
        except:
            nbSubNets = -1
        if nbSubNets <= 0 or nbSubNets > 10:
            vSubNets = True
            print("Warning : You entered an invalid number (you have to enter a number between > 0 and <= 10).")   
        else:
            vSubNets = False
    
    # nbUsers
    vUsers = True
    while vUsers:
        if vSubNets == 1:
            nbUsers = input("Enter the number of users you need for your SubNet : ")
        else :
            nbUsers = input("Enter the number of users (in descending order) for your " + str(nbSubNets) + " SubNets (ex : 300 200 100) : ")
        print("")

        nbUsers = nbUsers.split(' ')
        if len(nbUsers) > nbSubNets:
            vUsers = True
            print("Warning : You entered more than " + str(nbSubNets) + " SubNets.")
        elif len(nbUsers) < nbSubNets:
            vUsers = True
            print("Warning : You entered less than " + str(nbSubNets) + " SubNets.")
        else:
            vUsers = False

        if vUsers == False:
            check = False
            for i in range(nbSubNets):
                try:
                    nbUsers[i] = int(nbUsers[i])
                except:
                    nbUsers[i] = -1
                if nbUsers[i] <= 0 or nbUsers[i] > 4294967294:
                    check = True
                    print("Warning : You entered an invalid number (you have to enter numbers between > 0 and <= 4294967294).") 
                if i != 0 and nbUsers[i] > nbUsers[i-1]:
                    check = True
                    print("Warning : You must enter the number of users in descending order.")
            if check:
                vUsers = True
            else:
                vUsers = False



    # --- --- --- Subnets Loop --- --- --- #
    for nbSubNet in range(nbSubNets):

        # --- --- --- CIDR --- --- --- #
        # iCIDR
        iCIDR = 32
        while (2**(32-iCIDR) - 2) <= int(nbUsers[nbSubNet]):
            iCIDR = iCIDR - 1

        # --- --- --- Nbr of IPs --- --- --- #
        # nbIP
        nbIP = str(2**(32-iCIDR))
        if nbIP == '1':
            nbUsable = '1'
        else:
            nbUsable = str(2**(32-iCIDR) - 2)

        # --- --- --- Mask --- --- --- #
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

        # --- --- --- Network Address --- --- --- #
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

        
        # --- --- --- Check Nbr IPs Available --- --- --- # 
        # lDecRes
        # lDecBroad
        lDecRes = sDecRes.split('.')
        lDecBroad = sDecBroad.split('.')

        if lDecRes != lDecIP:
            print("Error : There isn't enough IPs ! Please reduce your numbers of users.")
            break

        # checkNbIp
        checkNbIp = 1
        for i in range(4):
            if int(lDecBroad[i]) - int(lDecRes[i]) != 0:
                checkNbIp = checkNbIp * (int(int(lDecBroad[i]) - int(lDecRes[i])) + 1)
        if int(nbIP) != checkNbIp:
            print("Error : There isn't enough IPs ! Please reduce your numbers of users.")
            break


        # --- --- --- Outputs --- --- --- #
        print("--- --- --- Network " + str(nbSubNet + 1) + " --- --- ---")
        print("Network Address : " + sDecRes)
        print("Broadcast Address : " + sDecBroad)
        print("Mask : " + sDecMask)
        print("CIDR : /" + str(iCIDR))
        print("")
        print("Number of IPs : " + nbIP)
        print("Number of usable IPs : " + nbUsable)
        print("")
        print("")

        # --- --- --- Update --- --- --- #
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
                    if int(lDecIP[0]) > 255: # DELETE ?
                        print("Error : There isn't enough IPs ! Please reduce your numbers of users.")
                        break


    # --- --- --- Exit or Continue --- --- --- #
    loop = input("If you want to continue press Enter else enter \"exit\" : ")
    print()
