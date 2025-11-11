try:
    list_of_numbers = list(map(int, input('Введите числа через пробел: ').split()))

    if 3 not in list_of_numbers:
        print('Список обязательно должен содержать значение 3!')
    else:
        new_list = []
        for num in list_of_numbers:
            if num != 3:
                new_list.append(num)
        print('Результат:', new_list)

except ValueError:
    print('Ошибка: вводите только целые числа!')
