sentence = input('Введите предложение: ').split()

new_list = []

for word in sentence:
    without_marks = word.strip('.,?!:;"\'()[]{}')
    new_list.append(without_marks)

print(new_list)
