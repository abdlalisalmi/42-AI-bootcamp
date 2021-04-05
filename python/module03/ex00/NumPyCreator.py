import numpy as np
import random
import string


class NumPyCreator:
    
    @staticmethod
    def change(data, dtype):
        if dtype == int:
            return int(data)
        elif dtype == float:
            return float(data)
        elif dtype == str:
            return str(data)
        return data


    @staticmethod
    def from_list(lst, dtype=None):
        return np.array([NumPyCreator.change(i, dtype) for i in lst])

    @staticmethod
    def from_tuple(tpl, dtype=None):
        return np.array([NumPyCreator.change(i, dtype) for i in tpl])


    @staticmethod
    def from_iterable(itr, dtype=None):
        return np.array([NumPyCreator.change(i, dtype) for i in itr])


    @staticmethod
    def from_shape(shape, value=0, dtype=None):
        matrix = []
        for i in range(0, shape[0]):
            vector = []
            for j in range(0, shape[1]):
                vector.append(NumPyCreator.change(value, dtype))
            matrix.append(vector)
        return np.array(matrix)


    @staticmethod
    def random(shape, dtype=None):
        letters = string.ascii_lowercase + string.ascii_uppercase
        digits = string.digits
        boths = digits + letters

        def array_generate(itr, chape, dtype):
            array = []
            for i in range(0, shape[0]):
                array.append([NumPyCreator.change(random.choice(itr), dtype) for i in range(0, chape[1])])
            return array

        if dtype == int:
            return np.array(array_generate(digits, shape, int))
        elif dtype == float:
            return np.array(array_generate(digits, shape, float))
        elif dtype == str:
            return np.array(array_generate(letters, shape, str))
        else:
            return np.array(array_generate(boths, shape, str))


    @staticmethod
    def identity(n, dtype=None):
        return np.identity(n, dtype=dtype)



if __name__ == '__main__':
    nc = NumPyCreator()
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(f"""
---------------- from_list ---------------
test case : {test}
Return    : {nc.from_list(test)}
------------------------------------------
""")

    print(f"""
---------------- from_tuble ---------------
test case : {tuple(test)}
Return    : {nc.from_list(test)}
------------------------------------------
""")

    print(f"""
---------------- from_iterable ---------------
test case : hello world!
Return    : {nc.from_list("hello world!")}
------------------------------------------
""")

    print(f"""
---------------- from_shape ---------------
test case : (4, 10)
Return    : {nc.from_shape((4, 5))}
------------------------------------------
""")

    print(f"""
---------------- random ---------------
test case : (4, 10)
Return    : {nc.random((4, 10))}
------------------------------------------
""")

    print(f"""
---------------- identity ---------------
test case : (4, 10)
Return    : {nc.identity(4)}
------------------------------------------
""")