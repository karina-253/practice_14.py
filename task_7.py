try:
    list_numbers = list(map(int, input('Введите целые'
                                       ' числа через пробел: ').split()))

    sum_even = sum(num for num in list_numbers if num % 2 == 0)
    sum_odd = sum(num for num in list_numbers if num % 2 != 0)

    print(sum_even, sum_odd)
except ValueError:
    print('Ошибка: вводите только целые числа!')
