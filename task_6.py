from typing import List, Union

def divisors(number: int) -> Union[List[int], str]:
    '''
    The function receives an integer and returns
    a list of the divisors of that number.

    Args:
        number (int): One integer number
    Returns:
        List[int]: list of the divisors of that number.
        str: if the number is zero.
    '''
    
    if number == 0:
        return 'Any non—zero number is a divisor of 0. '

    list_of_divisors = []

    for num in range(1, abs(number) + 1):
        if number % num == 0:
            list_of_divisors.append(num)

    return list_of_divisors

def main() -> None:
    number = int(input('Enter an integer: '))
    result = divisors(number)
    print(result)

if __name__ == "__main__":
    main()
