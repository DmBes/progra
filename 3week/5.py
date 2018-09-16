import math
n = float(input())
c = 0
if n % 1 != 0.5:
    c = round(n)
else:
    c = math.ceil(n)
print(c)
