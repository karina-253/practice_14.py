def has_hole(letter: str) -> bool:
    '''
    The function checks if the letter has a hole.

    Args:
        letter (str): The letter to check

    Returns:
        bool: True if the letter has a hole, False if not
    '''

    return letter in 'abdegopq'


def count_of_holes(word: str) -> int:
    '''
    The function counts the number of letters
     with holes in a word.

    Args:
        word (str): A word for analysis

    Returns:
        int: The number of letters with holes in a word
    '''

    count = 0

    for letter in word:
        if has_hole(letter):
            count += 1

    return count


def main() -> None:
  
    text = input().lower().split()

    let_with_hole = 0
    let_without_hole = 0
    words_with_holes = []

    for word in text:
        for let in word:
            if has_hole(let):
                let_with_hole += 1
            else:
                let_without_hole += 1

    for word in text:
        count_holes = count_of_holes(word)
        if count_holes >= 2:
            words_with_holes.append(word)

    print(f'Number of letters with holes: {let_with_hole}')
    print(f'Number of letters without holes:{let_without_hole}')
    print(f'Words with two or more holes: {words_with_holes}')


if __name__ == "__main__":
    main()
