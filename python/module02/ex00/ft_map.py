



def ft_map(function_to_apply, list_of_inputs):
    result = []
    for item in list_of_inputs:
        result.append(function_to_apply(item))
    return result



if __name__ == '__main__':

    def addition(n):
        return n + n

    l = [1, 2 , 3]
    print("\nCreate list of inputs:", l)

    print("\nDefine a functions 'addition' to use it in the test:")
    print("""
        def addition(n):
            return n + n  
""")
    
    print("Test map funtion: ")
    print("Result: ", list(map(addition, l)))
    print("\nTest ft_map funtion: ")
    print("Result: ", list(ft_map(addition, l)))
    print()