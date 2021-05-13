def is_palindrome(thing):
    if type(thing) != str:
        raise TypeError('argument must be a string')

    for i in range(len(thing) // 2):
        if thing[i] != thing[len(thing) - i - 1]:
            return False
    
    return True

if __name__ == '__main__':
    while True:
        thing = input('Enter a string to check: ')
        print(f'{thing} is a palindrome!') if is_palindrome(thing) else print(f'{thing} is not a palindrome.')
        if input('Try another string? (y/n): ') != 'y':
            break