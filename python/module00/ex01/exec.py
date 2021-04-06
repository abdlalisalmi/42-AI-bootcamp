import sys


def reverse(args):
    for arg in reversed(args):
        end = '\n' if arg == args[0] else ' '
        print(arg[::-1].swapcase(), end=end)


if __name__ == '__main__':
    reverse(sys.argv[1:])