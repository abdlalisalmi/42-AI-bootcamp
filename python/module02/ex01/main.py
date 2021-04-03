


def what_are_the_vars(*args, **keywargs):
    """Your code"""
    # print(args, keywargs)
    obj = ObjectC()
    if args or keywargs:
        if args:
            for i, value in zip(range(len(args)), args):
                setattr(obj, f"var_{i}", value)
        if keywargs:
            for key in keywargs.keys():
                if key.startswith('var_'):
                    return None
                else:
                    setattr(obj, key, keywargs.get(key))
    return obj


class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)

    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)

    obj = what_are_the_vars()
    doom_printer(obj)

    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)

    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)