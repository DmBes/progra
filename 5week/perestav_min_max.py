a = list(map(int, input().split()))
b = a.index(min(a))
c = a.index(max(a))
a[b], a[c] = a[c], a[b]
print(*a)
