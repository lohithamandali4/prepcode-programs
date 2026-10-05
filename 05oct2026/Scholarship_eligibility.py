percentage = int(input("Enter the percentage:"))
attendance = int(input("Enter the attendance:"))

if percentage >= 85 and attendance >= 75:
    print("eligible for scholarship")
else:
     print("not eligible for scholarship")