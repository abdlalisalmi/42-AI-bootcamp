

cookbook = {
    'sandwich': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 10
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'salad': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 15
    }
}


def interface():
    print("""Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit""")
    user = int(input(">> "))
    return user


def add_recipe():
    pass


def print_recipe():
    print("Please enter the recipe's name to get its details:")
    name = input(">> ")
    print(f"Recipe for {name}:")


def main():
    user = interface()
    if user == 1:
        add_recipe()
    elif user == 2:
        pass
    elif user == 3:
        print_recipe()
    elif user == 4:
        pass
    elif user == 5:
        print("Cookbook closed.")
        exit()
    else:
        print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")



if __name__ == '__main__':
    main()