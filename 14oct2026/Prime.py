number = int(input("Enter a number:"))
flag = True
for i in range(2,number):
    if number % i ==0:
        flag = False

    if flag == True:
        print("Prime number")
    else:
         print("not prime")