s = input()
a = s.find('f')
b = s.rfind('f')
print(a,b)
if a == -1:
    print()
elif a == b:
    print(a)
else:
    print(a, b)
