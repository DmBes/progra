x = float(input())
y = float(input())


def IsPointInSquare(z, c):
    return -1 <= z <= 1 and -1 <= c <= 1


if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")
