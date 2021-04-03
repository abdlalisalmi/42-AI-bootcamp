from functools import reduce


def ft_reduce(function_to_apply, list_of_inputs):
    first = list_of_inputs[0]
    for item in list_of_inputs[1:]:
        first = function_to_apply(first, item)
    return first



if __name__ == '__main__':

    def do_sum(n1, n2):
        return n1 + n2

    l = [1, 2 , 3]
    print("\nCreate list of inputs:", l)

    print("\nDefine a functions 'do_sum' to use it in the test:")
    print("""
--------------------------------------------
        def do_sum(n1, n2):
            return n1 + n2
--------------------------------------------
""")
    
    print("Test reduce funtion: ")
    print("Result: ", reduce(do_sum, l))
    print("\nTest ft_reduce funtion: ")
    print("Result: ", ft_reduce(do_sum, l))
    print()