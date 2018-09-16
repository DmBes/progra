a = list(map(int, input().split()))
k = list(map(int, input().split()))
a.insert(k[0], k[1])
print(*a)
