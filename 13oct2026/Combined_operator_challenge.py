price = 1000 
quantity = 2
is_member = True 
has_coupon = True

total = price * quantity

if is_member:
    total -= total * 10 / 100

if has_coupon:
    total -= price * quantity * 5 / 100

print("Final payable amount:", total)