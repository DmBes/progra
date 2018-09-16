def gen_bin(m, prefix=''):
    if m == 0:
        print(prefix)
        return
    else:
        gen_bin(m - 1, prefix + "0")
        gen_bin(m - 1, prefix + "1")




def generate_number(N:int, M:int, prefix=None):
    '''Генерирует все числа'''

    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N,M-1, prefix)
        prefix.pop()


generate_number(3,3)
#gen_bin(4)