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


# TEST
sDecIP = "192.168.0.0"
nbSubNets = 3
nbUsers = "200 100 6"

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
# check >0 and < 10

# nbUsers
nbUsers = nbUsers.split(' ')
# for nbUsers in nbUsers
# Check max hosts
# Check number of subnets == nbSubNets


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

    # lBinRes
    # lBinBroad
    lDecIP = list(sBinIP)
    lBinRes = []
    lBinBroad = []
    if iCIDR > 24:
        aCIDR = iCIDR + 3
    elif iCIDR > 16:
        aCIDR = iCIDR + 2
    elif iCIDR > 8:
        aCIDR = iCIDR + 1

    for i in range(35):
        if lDecIP[i] == '.':
            lBinRes.append('.')
            lBinBroad.append('.')
        else:
            if i < aCIDR and aCIDR != 0:
                lBinRes.append(lDecIP[i])
                lBinBroad.append(lDecIP[i])
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

    # --- --- --- Outputs --- --- --- #
    print("--- --- --- Network " + str(nbSubNet) + " --- --- ---")
    print("Network Address : " + sDecRes)
    print("Broadcast Address : " + sDecBroad)
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
    if lDecIP[3] > '255':
        lDecIP[2] = str(int(lDecIP[2]) + 1)
        if lDecIP[2] > '255':
            lDecIP[1] = str(int(lDecIP[1]) + 1)
            if lDecIP[1] > '255':
                lDecIP[0] = str(int(lDecIP[0]) + 1)
                if lDecIP[0] > '255':
                    # TODO Error out of range
                    print("Error")


# --- --- --- Exit or Continue --- --- --- #
#loop = input("If you want to quit enter \"exit\" else press Enter : ")
# print()
