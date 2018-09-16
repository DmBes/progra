x = float(input())
y = float(input())
xc = float(input())
xy = float(input())
r = float(input())


def IsPointInCircle(x, y, xc, xy, r):
    return (x - xc) ** 2 + (y - xy) ** 2 <= r ** 2


if IsPointInCircle(x, y, xc, xy, r):
    print("YES")
else:
    print("NO")
