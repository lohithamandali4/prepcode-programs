try:
    a = input("Enter Number 1: ")
    b = input("Enter Number 2: ")
    print(int(a)/int(b))
except valuError:
    print("Give the Numbers as a input")
except ZeroDivisionError:
    print("Cannot Divide by Zero")