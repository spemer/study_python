import getFruitNumber

#####START#####
def main():
    startMsg()
    getFruitQty()
    endMsg()

def startMsg():
    print("==========")
    print("Buy more than 3 grapes, get 10% discount!")
    print("==========\n")

#####GET NUMBERS#####
def getFruitQty():
    getAppleQty = int(input("Apple: "))
    getGrapeQty = int(input("Grape: "))
    getPeachQty = int(input("Peach: "))

    print("\n==========\n")

    if (getGrapeQty >= 3):
        print("You've buy more than 3 grapes, so you can get 10% discount.\n")

    elif (getGrapeQty < 3):
        print("You've buy less than 3 grapes, so you can't get 10% discount.\n")
        getGrapeQty_AGAIN = input("Do you want to revise amount of grape? Y/N: ")

        if (getGrapeQty_AGAIN.__contains__("Y") or getGrapeQty_AGAIN.__contains__("y")):
            getGrapeQty = int(input("Grape: "))

    print()
    print("Total Amount:", getFruitNumber.TOTALAMOUNT(getAppleQty, getGrapeQty, getPeachQty))
    print("Total Prices:", format(getFruitNumber.TOTALPRICES(getAppleQty, getGrapeQty, getPeachQty),',.0f'))

#####FINISH#####
def endMsg():
    print("\n==========")
    print("Thank you")
    print("==========")

main()
