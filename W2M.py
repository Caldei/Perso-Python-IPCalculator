"""
Content : Translator (Wildcard to Mask)
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
    print("Welcome : This is Wildcard Mask to Mask convertor !")

    # --- --- --- Input : Wildcard Mask --- --- --- #
    # lDecWMask
    vWMask = True
    while vWMask:
        sDecWMask = input("Enter a Wildcard Mask : ")
        print()
        if bool(re.match(IP_MASK_REGEX, sDecWMask)):
            lDecWMask = sDecWMask.split('.')
            check = False
            for i in range(4):
                if lDecWMask[i] != '255' and lDecWMask[i] != '127' and lDecWMask[i] != '63' and lDecWMask[i] != '31' and lDecWMask[i] != '15' and lDecWMask[i] != '7' and lDecWMask[i] != '3' and lDecWMask[i] != '1' and lDecWMask[i] != '0':
                    check = True
                    print("Warning : " +
                          lDecWMask[i] + " is not a valid byte.")
                elif i != 3 and lDecWMask[i] != '0' and lDecWMask[i+1] != '255':
                    check = True
                    print(
                        "Warning : This is not a valid Mask all bits must be right contiguous.")
            if check:
                vWMask = True
            else:
                vWMask = False
        else:
            vWMask = True
            print("Warning : This is not a valid WildCard Mask.")

    # --- --- --- Mask --- --- --- #
    # sDecMask
    sDecMask = ""
    for i in range(3):
        sDecMask = sDecMask + str(255 - int(lDecWMask[i]))
        sDecMask = sDecMask + '.'
    sDecMask = sDecMask + str(255 - int(lDecWMask[i+1]))

    # --- --- --- Bianary Mask --- --- --- #
    # lDecMask
    lDecMask = sDecMask.split('.')

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
    print("CIDR : " + sCIDR)
    print("Mask : " + sDecMask)
    print("Binary Mask : " + sBinMask)
    print()
    print("Number of IPs : " + nbIP)
    print("Number of usable IPs : " + nbUsable)
    print()
    print("Number of SubNets : " + nbSubNet)
    print()
    print()

    # --- --- --- Exit or Continue --- --- --- #
    loop = input("If you want to continue press Enter else enter \"exit\" : ")
    print()
