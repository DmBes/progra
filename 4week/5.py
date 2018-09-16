k = int(input())


def MinDivisor(n):
    import math
    c = 2
    while n % c != 0:
        if c >= math.sqrt(n):
            print(n)
            return

        c += 1
    print(c)
    return


MinDivisor(k)
