def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True

def showMenu():
    if login():
        print("Done !")
        print("----- iShop -----")
        print("1. Vat Calculator")
        print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        vatCalculator()
    elif userSelected == 2:
        priceCalculator()

def vatCalculator():
    price = int(input("Price (THB) : "))
    vat = 7
    result = price + (price * vat / 100)
    print(result)
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    print(price1 + price2)

###########################
showMenu()
menuSelect()





