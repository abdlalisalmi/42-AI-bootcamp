import sys

MORSE_CODE = {
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----'
}

def sos(args):
    for arg in args:
        for word in arg.split(' '):
            for c in word:
                print(MORSE_CODE.get(c.upper()), end=" ")
            print("", end="\n" if arg == args[-1] else "/ ")



if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        exit()
    for arg in args:
        for word in arg.split(' '):
            if not word.isalnum():
                print("ERROR")
                exit()

    sos(args)