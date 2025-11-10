def transformations(text: str) -> str:
    '''
    The function Converts a string into a list of characters,
     sorts it, and returns the string

    Args:
        text (str): The source string for processing
    Returns:
        str: returns the string received after transformations.
    '''

    list_of_chars = list(text)

    list_of_chars.sort()

    list_in_str = ''.join(list_of_chars)

    return list_in_str

def main() -> None:
    input_str = input('Введите строку: ')
    result = transformations(input_str)
    print(result)

if __name__ == "__main__":
    main()
