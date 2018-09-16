def merge(a: list, b: list):
    c = [0] * (len(a) + len(b))
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            n += 1
            k += 1
    while i < len(a):
        c[n] = a[i]
        n += 1
        i += 1
    while k < len(b):
        c[n] = b[k]
        n += 1
        k += 1
    return c

def merge_sort(a):
    "'Рекурсивная функцяия"
    if len(a) <= 1:
        return
    middle = len(a)//2
    L = [a[i] for i in range(0, middle)]
    R = [a[i] for i in range(middle, len(a))]
    merge_sort(L)
    merge_sort(R)
    c = merge(L, R)
    for i in range(len(a)):
        a[i] = c[i]



''''a = [1, 3, 5, 7, 4, 6, 3, 1, 1, 2, 3, 5]
b = [2, 4, 6, 8, 10, 12, 14]
"print(merge(a, b))"
merge_sort(a)
print(a)'''''



def hear_sort(a):
    if len(a) <= 1:
        return
    bareer = a[0]
    l = []
    m = []
    r = []
    for x in a:
        if x < bareer:
            l.append(x)
        elif x == bareer:
            m.append(x)
        else:
            r.append(x)
    k = 0
    hear_sort(l)
    hear_sort(r)
    for x in l+m+r:
        a[k] = x
        k += 1


q = [5, 212, 6, 4, 2]
hear_sort(q)
print(q)