APPLE = 2000
GRAPE = 3000
PEACH = 1000


#####GET TOTAL AMOUNT#####
def TOTALAMOUNT(getAppleQty, getGrapeQty, getPeachQty):
    fruitAmount = getAppleQty + getGrapeQty + getPeachQty

    return fruitAmount


#####GET TOTAL PRICES#####
def TOTALPRICES(getAppleQty, getGrapeQty, getPeachQty):
    ApplePrices = getAppleQty * APPLE
    GrapePrices = getGrapeQty * GRAPE
    PeachPrices = getPeachQty * PEACH

    originalPrices = ApplePrices + GrapePrices + PeachPrices

    if (getGrapeQty >= 3):
        fruitPrices = originalPrices - (originalPrices / 10)
        return fruitPrices

    elif (getGrapeQty < 3):
        fruitPrices = originalPrices
        return fruitPrices
