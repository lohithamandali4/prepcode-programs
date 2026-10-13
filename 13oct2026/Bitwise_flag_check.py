permissions = 7
read_permission = 4

if permissions & read_permission:
    print("Read permissions is enabled")
else:
    print("Read permissions is disabled")