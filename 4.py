def sumBase(k,n = 10):
    s = 0
    while n > 0:
        s += (n % k)
        n = n // k
    return s

x = int(input("n: "))
y = int(input("k: "))
print(sumBase(y,x))