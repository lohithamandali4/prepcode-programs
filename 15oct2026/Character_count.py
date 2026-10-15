s = input("Enter a string: ")

s = s.lower().replace(" ", "")

if s == s[: :-1]:
    print("True")
else:
    print("False")