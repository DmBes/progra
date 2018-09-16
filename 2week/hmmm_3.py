n = -1
f = 0
k = 0
while n != 0:
    n = int(input())
    if n > f:
        f = n
        k = 1
    elif n == f:
        k += 1
    else:
        continue
print(k)
