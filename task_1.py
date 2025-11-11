try:
    numbers = list(map(int, input('Введите 10 целых чисел через пробел: ').split()))

    if len(numbers) != 10:
        print('Ошибка: нужно ввести ровно 10 чисел!')
    else:
        new_list = []
        for i in range(1, 9):
            new_list.append(numbers[i - 1] + numbers[i + 1])
        print('Результат:', new_list)

except ValueError:
    print('Ошибка: вводите только целые числа!')
    
