text = "hello world"

vowels = 0
digits = 0
others = 0

for ch in text:
    if ch.lower() in 'aeiou':
        vowels += 1
    elif ch.isdigit():
         digits += 1
    elif ch.isalpha():
         others == 1

print("vowels:", vowels)
print("digits:", digits)
print("other letters:", others)