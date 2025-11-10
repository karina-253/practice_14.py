lst_1 = list(map(int, input('Введите целые числа через пробел:').split()))
lst_2 = list(map(int, input('Введите целые числа через пробел:').split()))
range_lst1 = input('Введите диапазон элементов в первом списке:').split()

first = int(range_lst1[0])
second = int(range_lst1[1])

deleted_elements = lst_1[first - 1:second][::-1]

lst_2 += deleted_elements

del lst_1[first - 1:second]

print(lst_1)
print(lst_2)
