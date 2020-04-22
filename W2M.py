"""
Content : Translator (Wildcard to Mask and CIDR)
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
    print("Welcome : This is Wildcard Mask to Mask convertor !")

    # --- --- --- Input : Wildcard Mask --- --- --- #
    # input -> Verification then Decimal WildCard Mask List -> lDecWMask
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

    # --- --- --- Calculation : Mask --- --- --- #
    # lDecWMask -> Decimal WildaCard Mask List to Decimal Mask String -> sDecMask
    sDecMask = ""
    for i in range(3):
        sDecMask = sDecMask + str(255 - int(lDecWMask[i]))
        sDecMask = sDecMask + '.'
    sDecMask = sDecMask + str(255 - int(lDecWMask[i+1]))

    # sDecMask -> Decimal Mask String to Decimal Mask List -> lDecMask
    lDecMask = sDecMask.split('.')

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
    print("Mask : " + sDecMask)
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
