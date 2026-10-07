order_amount = 1200
premium_member = True

free_delivery = order_amount >= 1000 or premium_member

print("free delivery:",free_delivery)