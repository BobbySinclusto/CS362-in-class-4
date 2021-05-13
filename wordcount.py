import re

def wordcount(sentence):
    if type(sentence) != str:
        raise TypeError('argument must be a string')

    return len(re.findall(r'(\S+)', sentence))

if __name__ == '__main__':
    while True:
        thing = input('Enter a sentence to count the words in: ')
        print(f'There are {wordcount(thing)} words in your sentence.')
        if input('Try another string? (y/n): ') != 'y':
            break