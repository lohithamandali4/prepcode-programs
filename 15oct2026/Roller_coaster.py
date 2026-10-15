age = int(input("Enter your age:"))
height = int(input("Enter your height:"))
weight = int(input("Enter your weight:"))

if age > 18 and age < 50:
    if height > 150 and height < 210:
        if weight > 45 and weight < 110:
            print("Eligible to ride:")
        else: 
            print("Not eligible to ride:")
    else:
        print("Eligible to ride")
else:
    print("Not eligible to ride")