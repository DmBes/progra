a = list(map(int, input().split()))
b = 0
for i in range(1, len(a)):
    if a[i] != a[i-1]:
        b += 1
print(b+1)
