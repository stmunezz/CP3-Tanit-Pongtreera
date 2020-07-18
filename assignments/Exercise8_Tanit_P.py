userName = "User"
passWord = "123456"
userInput = input()
passInput = input()
sumPrice = 0

if userInput == userName and passInput == passWord:
    print("=====Welcome=====")
    print("Item list")
    print("1 banana     ", 200, "THB")
    print("2 apple      ", 50, "THB")
    print("3 Pineapple  ", 30, "THB")
    print("4 Papaya     ", 90, "THB")
    print("5 Coconut    ", 40, "THB")
    print("6 Melon      ", 90, "THB")
    n = int(input("Select item > "))
    numItem = int(input("Number of item > "))
    if n == 1:
        sumPrice = 200 * numItem
    elif n == 2:
        sumPrice = 50 * numItem
    elif n == 3:
        sumPrice = 30 * numItem
    elif n == 4:
        sumPrice = 90 * numItem
    elif n == 5:
        sumPrice = 40 * numItem
    elif n == 6:
        sumPrice = 90 * numItem

    if sumPrice == 0:
        print("ERROR")
    else:
        print("Price = ", sumPrice, "THB")

else:
    print("ERROR")

