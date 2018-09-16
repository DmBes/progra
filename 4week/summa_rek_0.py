def qwer():
    a = int(input())
    if a != 0:
        return a + qwer()
    return a


print(qwer())
