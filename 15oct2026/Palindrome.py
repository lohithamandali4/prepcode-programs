s = input("Enter a string: ")

s = s.lower()
s = "".join(ch for ch in s if ch.isalnum())

if s == s[: :-1]:
    print("Palindrome")
else:
    print("Not a palindrome")