sentence = input('Введите предложение: ').split()

without_marks = [word.strip('.,?!:;"\'()[]{}').lower()
                 for word in sentence]

new_list = []

for word in without_marks:
    if word not in new_list:
        new_list.append(word)

print(new_list)
