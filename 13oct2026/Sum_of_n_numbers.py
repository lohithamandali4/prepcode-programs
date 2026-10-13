def fibo(n): 
    if n<= 0:
        return 0

    return fibo(n-1) + n
print (fibo(4))
