try:
    numbers = list(map(int, input('Введите целые'
                                  ' числа через пробел: ').split()))

    average_value = sum(numbers) / len(numbers) if numbers else 0

    print(f'Среднее значение: {average_value}')
except ValueError:
    print('Ошибка: вводите только целые числа!')
