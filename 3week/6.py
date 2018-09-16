import math
p = int(input())
x = int(input())
y = int(input())
p += 100
s = ((y + x * 100) * p) / 100
s = int(s)
g = s // 100
h = s % 100

print(g, h)
