try:
    lst_1 = list(map(int, input('Введите числа через пробел:').split()))
    command = input('Введите команду: "R"+цифра для сдвига вправо'
                    'или "L"+цифра для сдвига влево:')

    side = command[0]
    shift = int(command[1:])

    if side == 'R':
        lst_1 = lst_1[-shift:] + lst_1[:-shift]
        print(lst_1)

    elif side == 'L':
        lst_1 = lst_1[shift:] + lst_1[:shift]
        print(lst_1)
except ValueError:
    print('Ошибка ввода!')
