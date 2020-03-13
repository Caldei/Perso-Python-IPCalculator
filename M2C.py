"""
Content : Translator (Mask to CIDR)
Using : Python

Author : Arthur
Date : March 2020
Context : Personal
"""

# Import
import re

# Loop
loop = ""
while loop != "exit":
    print("Welcome : This is Mask to CIDR convertor !")

    # Input
    vDecMask = True
    while vDecMask:
        sDecMask = input("Enter a Mask : ")
        print("")
        if bool(re.match("^([0-9]{1,3}\.){3}[0-9]{1,3}$", sDecMask)):
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
                vDecMask = True
            else:
                vDecMask = False
        else:
            vDecMask = True
            print("Warning : This is not a valid Mask.")

    # Wildcard Mask String
    sDecWMask = ""
    for i in range(3):
        sDecWMask = sDecWMask + str(255 - int(lDecMask[i]))
        sDecWMask = sDecWMask + '.'
    sDecWMask = sDecWMask + str(255 - int(lDecMask[i+1]))

    # Bianary Mask string
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

    # CIDR
    lDecMask = list(sBinMask)
    dCIDR = 0
    for i in range(len(lDecMask)):
        if lDecMask[i] == '1':
            dCIDR = dCIDR + 1
    sCIDR = "/" + str(dCIDR)

    # Output
    print("Wildcard Mask : " + sDecWMask)
    print("Binary Mask : " + sBinMask)
    print("CIDR : " + sCIDR)
    print("")

    # Exit or Continue
    print("If you want to quit enter \"exit\" else press Enter")
    loop = input()
