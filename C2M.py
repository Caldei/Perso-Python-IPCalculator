"""
Content : Translator (CIDR to Mask and Wildcard Mask)
Using : Python

Author : Arthur
Date : March 2020
Context : Personal
"""


# --- --- --- Program Loop : Start --- --- --- #
loop = ""
while loop != "exit":
    print("Welcome : This is CIDR to Mask convertor !")

    # --- --- --- Input : CIDR --- --- --- #
    # Input -> Verification then CIDR Integer -> iCIDR
    vCIDR = True
    while vCIDR:
        sCIDR = input("Enter a CIDR (just the number) : ")
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

    # --- --- --- Calculation : Mask and WildCard Mask --- --- --- #
    # iCIDR -> CIDR Integer to Binary Mask List -> lBinMask
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

    # lBinMask -> List to String -> sBinMask
    sBinMask = "".join(lBinMask)

    # lBinMask -> Binary Mask List to Decimal Mask String -> sDecMask
    # lBinMask -> Binary Mask List to Decimal WildaCard Mask String -> sDecWMask
    sDecMask = ""
    sDecWMask = ""
    mOctet = 0
    wOctet = 0
    p = 7
    for i in range(35):
        if lBinMask[i] == '1':
            mOctet = mOctet + 2**p
            p = p - 1
        elif lBinMask[i] == '0':
            wOctet = wOctet + 2**p
            p = p - 1
        else:
            sDecMask = sDecMask + '.'
            sDecWMask = sDecWMask + '.'
        if p < 0:
            sDecMask = sDecMask + str(mOctet)
            sDecWMask = sDecWMask + str(wOctet)
            mOctet = 0
            wOctet = 0
            p = 7

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
    print("Decimal Mask : " + sDecMask)
    print("Wildcard Mask : " + sDecWMask)
    print("Binary Mask :  " + sBinMask)
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
