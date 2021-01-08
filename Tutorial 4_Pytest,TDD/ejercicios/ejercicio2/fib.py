def fibo(n):
    o,n = 0 , 1
    for _ in range (n):
        o,n = n,o + n
    return o