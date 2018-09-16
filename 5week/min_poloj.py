a = list(map(int, input().split()))
b = []
for i in range(len(a)):
    if a[i] > 0:
        b.append(a[i])
print(min(b))
