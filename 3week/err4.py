s = input()
a = s.find('f')
b = (s.find('f', a+1))
if b > 0 and a >= 0:
    print(s.find('f', a + 1))
elif a >= 0:
    print(-1)
else:
    print(-2)
