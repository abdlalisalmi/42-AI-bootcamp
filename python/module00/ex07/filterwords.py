import sys
from string import punctuation


def filter_words(string, n):
    words = [(word) for word in string.split(' ') if len(word) > int(n) ]
    result = []
    for word in words:
        for c in punctuation:
            word = word.replace(c, "")
        result.append(word.replace(c, ""))
    print(result)


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 2 or not args[1].isdecimal() or args[0].isdecimal():
        print("ERROR")
    else:
        filter_words(args[0], args[1])

