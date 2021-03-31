import sys

def usage(error=None):
    print(f"""{error if error else ""}Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3""")


def operations(num1, num2):
    print(f"""Sum:         {num1 + num2}
Difference:  {num1 - num2}
Product:     {num1 * num2}
Quotient:    {num1 / num2 if num2 != 0 else "ERROR (div by zero)"}
Remainder:   {num1 % num2 if num2 != 0 else "ERROR (modulo by zero)"}
""")


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        usage()
    elif len(args) < 2:
        usage("InputError: few arguments\n\n")
    elif len(args) > 2:
        usage("InputError: too many arguments\n\n")
    elif len(args) == 2:
        if not args[0].isdecimal() or not args[1].isdecimal():
            usage("InputError: only numbers\n\n")
        else:
            operations(int(args[0]), int(args[1]))