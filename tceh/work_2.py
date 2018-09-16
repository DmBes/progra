def all_numbers(*numbers):
    is_numbers = True
    for num in numbers:
        if isinstance(num, float):
            is_numbers = is_numbers and True
        else:
            is_numbers = is_numbers and False
 
    return is_numbers
 
 
def operation(x, y, sign):
    if sign == '+':
        return x + y
    elif sign == '-':
        return x - y
 
num1 = float(input('Введите 1ое число : '))
num2 = float(input('Введите 2ое число : '))
 
sign = ''
while (sign != '+') and (sign != '-'):
    sign = input('Введите знак "+" или "-" : ')
 
if all_numbers(num1, num2):
    print('Результат {} {} {} = {}'.format(num1, sign, num2, operation(num1, num2, sign)))