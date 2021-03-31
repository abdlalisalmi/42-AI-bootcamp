

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
    while True:
        try:
            user = int(input(">> "))
            if not user in range(1, 6):
                raise ValueError
            else:
                break
        except ValueError:
            print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
    return user


def add_recipe():
    recipe_name = input("Please enter the recipe name: ")
    ingredients = input("Please enter the ingredients list (ingre1, ingre2, ...): ")
    meal = input("Please enter the meal: ")
    prep_time = input("Please enter the preparation time in minutes: ")

    cookbook.update({
        recipe_name: {
            'ingredients': [ing.strip() for ing in ingredients.split(',')],
            'meal': meal,
            'prep_time': prep_time
        }
    })
    print(f"The recipe {recipe_name} created successfully.")
    main()


def delete_recipe():
    while True:
        recipe_name = input("Please enter the recipe name you want to delete. Or Q to quit\n>> ")
        if recipe_name.lower() == 'q':
            main()
        try:
            print(f"Delete recipe {recipe_name}...")
            cookbook.pop(recipe_name)
            main()
            break
        except:
            print(f"Recipe with name {recipe_name} doesn't exist!")


def print_recipe():
    print("Please enter the recipe's name to get its details:")
    name = input(">> ")
    recipe = cookbook.get(name, None)
    if recipe:
        print(f"Recipe for {name}:")
        print(f"Ingredients list: {recipe.get('ingredients')}")
        print(f"To be eaten for {recipe.get('meal')}")
        print(f"Takes {recipe.get('prep_time')} minutes of cooking")
        main()
    else:
        print(f"Recipe with name {name} doesn't exist!")
        print_recipe()


def print_cookbook():
    for recipe in cookbook.keys():
        print(f"Recipe for {recipe}:")
        print(f"\tIngredients list: {cookbook.get(recipe).get('ingredients')}")
        print(f"\tTo be eaten for {cookbook.get(recipe).get('meal')}")
        print(f"\tTakes {cookbook.get(recipe).get('prep_time')} minutes of cooking\n")
    main()


def main():
    user = interface()
    if user == 1:
        add_recipe()
    elif user == 2:
        delete_recipe()
    elif user == 3:
        print_recipe()
    elif user == 4:
        print_cookbook()
    elif user == 5:
        print("\nCookbook closed.")
        exit()
    else:
        print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")



if __name__ == '__main__':
    main()