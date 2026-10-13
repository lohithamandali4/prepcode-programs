balance = 10000
amount = 5000

if amount <= balance and amount % 500 == 0:
    print("Transaction allowed")
else:
    print("Transaction denied")