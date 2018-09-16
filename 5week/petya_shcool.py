a = list(map(int, input().split()))
b = int(input())
pos = 0
while pos < len(a) and b <= a[pos]:
    pos += 1
print(pos+1)
