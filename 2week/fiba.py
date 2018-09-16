n = int(input())
a1 = 1
a2 = 0
s = 0

if n > 1:
    while n != 1:
        s = (a1 + a2)
        a2 = a1
        a1 = s
        n -= 1
elif n == 1:
    s = a1
else:
    s = 0
print(s)
