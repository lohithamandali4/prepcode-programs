s = input("Enter a string: ")

found = False

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating character:", ch)
        found = True
        break

if not found:
    print("No non repeating character")