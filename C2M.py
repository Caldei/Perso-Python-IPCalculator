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
        CIDR = input("Enter a CIDR (just the number): ")
        print("")
        try:
            CIDR = int(CIDR)
        except:
            CIDR = -1
        if CIDR < 0 or CIDR > 32:
            vCIDR = True
            print("Warning : CIDR must be a number between 0 and 32.")
        else:
            vCIDR = False


    # Bianary Mask list
    lBinMask = []
    for i in range(32):

        if i < CIDR:
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


    # Decimal Mask string
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
