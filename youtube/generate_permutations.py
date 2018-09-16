def find(number,A):
    ''' ищут Number  в А b возвращает True, если
    такой есть и False если нет'''
    for x in A:
        if number == x:
            return True
    return False


def generate_per(N:int, M:int=-1, prefix=None):
    """Генерация всех перестановок"""
    M = N if M ==-1 else M # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_per(N, M-1, prefix)
        prefix.pop()


generate_per(3)
