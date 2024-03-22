print("Amount Due: 50")
amount = 50
price = 0
while amount>1:
    coin = int(input("Insert Coin: "))
    if coin==25 or coin == 10 or coin == 5:
        amount -= coin
    if amount>0:
        print("Amount Due:",amount)
print("Change Owed:",abs(amount))


    
    