def fibo(n):
    if n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)

def listFibo(n):
    for i in range(1, n+1):
        print(fibo(i), end='\t')

print(fibo(6))
listFibo(6)