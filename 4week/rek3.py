a = float(input())
n = int(input())


def quad(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return a * quad(a, n - 1)
    else:
        return a * quad(a, n - 1)


print(quad(a, n))
