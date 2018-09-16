def pr():
    n = int(input())
    if n == 0:
        print(n)

    else:
        print(n)
        return pr()


pr()
print(pr())
