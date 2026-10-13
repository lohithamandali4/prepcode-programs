blocked_usernames = ["admin", "root", "guest"]
username = "lohi"

if username not in blocked_usernames:
    print("username is allowed")
else:
    print("username is blocked")