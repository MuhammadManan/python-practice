def even_odd(num):
    '''
    Function to determine if a number is even or odd.
    :param num: Integer number to check
    :return: "Even" if the number is even, "Odd" if the number is odd.
    '''
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
# number = int(input("Enter a number: "))
# print(f"{number} is {even_odd(number)}")