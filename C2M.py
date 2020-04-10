"""
Content : Translator (CIDR to Mask)
Using : Python

Author : Arthur
Date : March 2020
Context : Personal
"""


# --- --- --- Loop --- --- --- #
loop = ""
while loop != "exit":
    print("Welcome : This is CIDR to Mask convertor !")

    # --- --- --- Input : CIDR --- --- --- #
    # iCIDR
    vCIDR = True
    while vCIDR:
        sCIDR = input("Enter a CIDR (just the number): ")
        print()
        try:
            iCIDR = int(sCIDR)
        except:
            iCIDR = -1
        if iCIDR < 0 or iCIDR > 32:
            vCIDR = True
            print("Warning : CIDR must be a number between 0 and 32.")
        else:
            vCIDR = False

    # --- --- --- Mask and WildCard Mask --- --- --- #
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

    # sBinMask
    sBinMask = ""
    for i in range(35):
        sBinMask = sBinMask + str(lBinMask[i])

    # sDecMask
    # sDecWMask
    sDecMask = ""
    sDecWMask = ""
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
            sDecWMask = sDecWMask + '.'
        if p < 0:
            sDecMask = sDecMask + str(octet)
            sDecWMask = sDecWMask + str(wOctet)
            octet = 0
            wOctet = 0
            p = 7

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
    print("Decimal Mask : " + sDecMask)
    print("Wildcard Mask : " + sDecWMask)
    print("Binary Mask :  " + sBinMask)
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
