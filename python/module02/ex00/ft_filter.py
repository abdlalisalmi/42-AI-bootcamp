


from typing import NoReturn


def ft_filter(function_to_apply, list_of_inputs):
    if not function_to_apply:
        return [item for item in list_of_inputs if item]
    else:
        return [item for item in list_of_inputs if function_to_apply(item)]
    



if __name__ == '__main__':

    # function that filters vowels
    def filter_vowels(letter):
        vowels = ['A', 'E', 'I', 'O', 'U']
        if(letter in vowels):
            return True
        return False

    letters = [   'A', 'B', 'C', 'D', 'E', 'F', 'G', 
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
            'V', 'W', 'X', 'Y', 'Z', False
        ]
    print("\nCreate list of inputs:", letters)

    print("\nDefine a functions 'filter_vowels' to use it in the test:")
    print("""
-------------------------------------------------
        def filter_vowels(letter):
            vowels = ['a', 'e', 'i', 'o', 'u']
            if(letter in vowels):
                return True
            return False
-------------------------------------------------
""")
    filtered_list = filter(filter_vowels, letters)
    print("Test filter funtion: ")
    print("Result: ", list(filtered_list))

    filtered_list = ft_filter(filter_vowels, letters)
    print("\nTest ft_filter funtion: ")
    print("Result: ", list(filtered_list))
    print()