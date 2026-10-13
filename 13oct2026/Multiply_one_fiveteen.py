def fibo (n):
    if n <= 1:
        return 1

    return fibo(n-1)*n
print(fibo(5))