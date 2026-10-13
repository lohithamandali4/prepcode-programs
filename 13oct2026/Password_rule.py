password = "hello@123"

valid = len(password) >= 8 and any(not ch.isalnum() for ch in password)

print("valid password:",valid)