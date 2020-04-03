"""
Content : Translator (Mask to CIDR)
Using : Python

Author : Arthur
Date : March 2020
Context : Personal
"""


# --- --- --- Imports --- --- --- #
import re


# --- --- --- Constant --- --- --- #
IP_MASK_REGEX = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"


# --- --- --- Loop --- --- --- #
loop = ""
while loop != "exit":
    print("Welcome : This is Mask to CIDR convertor !")

    # --- --- --- Inputs --- --- --- #
    # lDecMask
    vMask = True
    while vMask:
        sDecMask = input("Enter a Mask : ")
        print("")
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

    # --- --- --- Wildcard Mask --- --- --- #
    # sDecWMask
    sDecWMask = ""
    for i in range(3):
        sDecWMask = sDecWMask + str(255 - int(lDecMask[i]))
        sDecWMask = sDecWMask + '.'
    sDecWMask = sDecWMask + str(255 - int(lDecMask[i+1]))

    # --- --- --- Bianary Mask --- --- --- #
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

    # --- --- --- CIDR --- --- --- #
    # sCIDR
    lDecMask = list(sBinMask)
    iCIDR = 0
    for i in range(len(lDecMask)):
        if lDecMask[i] == '1':
            iCIDR = iCIDR + 1
    sCIDR = "/" + str(iCIDR)

    # --- --- --- Nbr of IPs --- --- --- #
    # nbIP
    nbIP = str(2**(32-iCIDR))
    if nbIP == '1':
        nbUsable = '1'
    else:
        nbUsable = str(2**(32-iCIDR) - 2)

    # --- --- --- Nbr of SubNets --- --- --- #
    # nbIP
    nbSubNet = str(2**(32-iCIDR-2))
    if nbSubNet < '1':
        nbSubNet = '1'

    # --- --- --- Outputs --- --- --- #
    print("Wildcard Mask : " + sDecWMask)
    print("Binary Mask : " + sBinMask)
    print("CIDR : " + sCIDR)
    print("")
    print("Number of IPs : " + nbIP)
    print("Number of usable IPs : " + nbUsable)
    print("")
    print("Number of SubNets : " + nbSubNet)
    print("")
    print("")

    # --- --- --- Exit or Continue --- --- --- #
    loop = input("If you want to continue press Enter else enter \"exit\" : ")
    print()
