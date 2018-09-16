a = int(input())
b = a
k = 0
c = 0
while a != 0:
    if a == b:
        k += 1
    elif a != b:
        if c <= k:
            c, k = k, c
            k = 1
        else:
            k = 1
    b = a
    a = int(input())
if c <= k:
    c, k = k, c
print(c)
