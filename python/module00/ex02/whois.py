import sys




def whois(arg):
    if len(arg) < 1:
        return
    elif len(arg) > 1 or not arg[0].isdigit():
        print("ERROR")
        return

    numbre = int(arg[0])

    if numbre == 0:
        print("I'm Zero.")
    elif numbre % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
    

if __name__ == '__main__':
    whois(sys.argv[1:])