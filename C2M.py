"""
Content : Translator (CIDR to Mask)
Using : Python

Author : Arthur
Date : March 2020
Context : Personal
"""

# Loop
loop = ""
while loop != "exit":
    print("Welcome : This is CIDR to Mask convertor !")

    # Input
    vCIDR = True
    while vCIDR:
        sCIDR = input("Enter a CIDR (just the number): ")
        print("")
        try:
            dCIDR = int(sCIDR)
        except:
            dCIDR = -1
        if dCIDR < 0 or dCIDR > 32:
            vCIDR = True
            print("Warning : CIDR must be a number between 0 and 32.")
        else:
            vCIDR = False

    # Bianary Mask list
    lBinMask = []
    for i in range(32):
        if i < dCIDR:
            if i % 8 == 0 and i != 0:
                lBinMask.append('.')
            lBinMask.append(1)
        else:
            if i % 8 == 0 and i != 0:
                lBinMask.append('.')
            lBinMask.append(0)

    # Bianary Mask string
    sBinMask = ""
    for i in range(35):
        sBinMask = sBinMask + str(lBinMask[i])

    # Bianary Mask string (Other Method)
    #sBinMask = str(lBinMask)
    #sBinMask = sBinMask.replace('[', '')
    #sBinMask = sBinMask.replace(']', '')
    #sBinMask = sBinMask.replace(',', '')
    #sBinMask = sBinMask.replace(' ', '')
    #sBinMask = sBinMask.replace('\'', '')

    # Decimal Mask and WildCard Mask strings
    sDecMask = ""
    sDecWMask = ""
    octet = 0
    wOctet = 0
    p = 7
    for i in range(35):
        if lBinMask[i] == 1:
            octet = octet + 2**p
            wOctet = wOctet + 0
            p = p - 1
        elif lBinMask[i] == 0:
            octet = octet + 0
            wOctet = wOctet + 2**p
            p = p - 1
        else:
            sDecMask = sDecMask + '.'
            sDecWMask = sDecWMask + '.'
        if p < 0:
            sDecMask = sDecMask + str(octet)
            sDecWMask = sDecWMask + str(wOctet)
            octet = 0
            wOctet = 0
            p = 7

    # Outpout
    print("Binary Mask :  " + sBinMask)
    print("Decimal Mask : " + sDecMask)
    print("Wildcard Mask : " + sDecWMask)
    print("")

    # Exit or Continue
    print("If you want to quit enter \"exit\" else press Enter")
    loop = input()
