n = int(input())
k = 0
f = n
while n != 0:
    if f < n:
        k += 1
    f = n
    n = int(input())
print(k)
