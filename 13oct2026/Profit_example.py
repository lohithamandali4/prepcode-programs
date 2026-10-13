buying_price = int(input("Enter the buying_price:"))
selling_price = int(input("Enter the amount you sold for:"))
total_product = int(input("Enter the amount of products:"))
storage_price = int(input("storage amount:"))

profit = ((selling_price - buying_price) * total_product) - storage_price

print(f"total profit: {profit}")