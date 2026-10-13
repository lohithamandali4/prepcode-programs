def div(n):
    if n <= 3:
         return 0 
    if n % 3 == 0 and n % 5 == 0:
        return n + div(n-1)
    else:
         return div(n-1)
print(div(100))