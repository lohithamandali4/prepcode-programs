price = 500
quantity = 2
delivery_charge = 50
discount = 10

final_bill = price * quantity + delivery_charge - (price * quantity * discount / 100)

print("Final bill:", final_bill)