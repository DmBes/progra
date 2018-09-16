a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - (a * 4 * c)
if d == 0:
    x = -1 * (b / (2 * a))
    print(x)
elif d > 0:
    x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    if x > x1:
        x1, x = x, x1
    print('{0:.6f}'.format(x), '{0:.6f}'.format(x1))
