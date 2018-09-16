s = list(map(int, input().split()))
n = []
for i in range(s[1]):
    b = int(input())
    n.append(b)
n = sorted(n)
k = 0
for r in range(len(n)):
    if s[0] >= n[r]:
        s[0] = s[0] - n[r]
        k += 1
print(k)
