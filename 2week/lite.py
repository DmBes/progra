a = int(input())
b = 0
while a != 0:
    if a > b:
        a, b = b, a
    a = int(input())
print(b)
