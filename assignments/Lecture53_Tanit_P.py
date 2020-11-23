priceInput = int(input())

def vatCal(price):
    result = price + (price*0.07)
    return result

print(vatCal(priceInput))

