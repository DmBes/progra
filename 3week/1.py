a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
s = p * (p - a) * (p - b) * (p - c)
print('{0:.6f}'.format(s ** 0.5))
