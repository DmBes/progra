def IsPrime(n):
    import math
    d = 2
    while n % d != 0 and d <= int(math.sqrt(n)):
        d += 1
    return d > math.sqrt(n)


n = int(input())
if IsPrime(n):
    print("YES")
else:
    print("NO")
