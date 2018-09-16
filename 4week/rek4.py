def ReduceFraction(n, m):
    z = n
    if m % z == 0 and n % z == 0:
        return print(n / n, m/n)

    else:
        return ReduceFraction()


n = int(input())
m = int(input())
ReduceFraction(n, m)
