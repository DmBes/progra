n = int(input())
s = 0
while n != 0:
    s += float(1 / (n ** 2))
    n -= 1
print('{0:.6f}'.format(s))
if n != 0:
    print('end')