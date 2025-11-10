def word_without_marks(word: str) -> str:
    '''
    The function Clears the word from punctuation
     marks and lowercase it.

    Args:
        word (str): The source word for processing

    Returns:
        str: The cleared word is in lowercase
    '''

    final_word = word.strip('.,?!:;"\'()[]{}')

    return final_word.lower()

order = []
count = {}

while True:
    text = input()
    if text == '':
        break

    line = text.split()

    for word in line:
        final_word = word_without_marks(word)

        if final_word:
            if final_word not in count:
                count[final_word] = 0
                order.append(final_word)
            count[final_word] += 1

sorted_words = sorted(count.keys(), key=lambda word:
(-count[word], order.index(word)))

for word in sorted_words:
    print(word)
