x = int(input('введите первое число: '))
y = int(input('введите второе число: '))
deistvie = input('введите математическое действие: ')
if deistvie == '+':
    print(x + y)
elif deistvie == '-':
    print(x - y)
elif deistvie == '*':
    print(x * y)
elif deistvie == '/':
    print(x/y)