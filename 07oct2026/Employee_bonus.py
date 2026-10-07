rating = float(input("enter performance rating"))

years = int(input("enter years in company:"))

if rating >= 4 and years >= 2:
    print("eligible for bonus")
else:
    print("not eligible for bonus")
    