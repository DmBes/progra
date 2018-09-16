a = float(input())
n = int(input())


def power(a, n):
    if n == 0:
        return 1
    else:
        n -= 1
        return n + power(a, n)


print(power(a, n))
