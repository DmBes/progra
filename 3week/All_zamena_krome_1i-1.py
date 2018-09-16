a = str(input())
k = a.find("h")+1
s = a.rfind('h')
if a.count('h') > 2:
    t = a[k: s].replace('h', 'H')
    print(a[:k]+t+a[s:])
else:
    print(a)
