a = float(input())
n = int(input())
c = a
d = 1


def power(a, n, d):

    if n == 0:
        return 1
    else:
        while d != n:
            a *= c
            d += 1
            power(a, n, d)
        return a


print(power(a, n, d))
