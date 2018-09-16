a = int(input())
b = int(input())
c = int(input())
d = int(input())


def min4(a, b):
    if a > b:
        a, b = b, a
        return b
    return b



print(min4(a, min4(b, min4(c, d))))
