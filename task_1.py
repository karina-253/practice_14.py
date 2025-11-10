numbers = list(map(int, input('Введите 10 целых чисел: ').split()))

if len(numbers) != 10:
    print('Введите ровно 10 чисел!')
else:
    new_list = []

    for i in range(1, 9):
        new_list.append(numbers[i-1]+numbers[i+1])

    print(new_list)
