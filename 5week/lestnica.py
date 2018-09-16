n = int(input())

for i in range(1, n + 1):
    for k in range(1, n):
        if k <= i-1:
            print(k, end='')
    print(i)
