


class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, recipe_type, ingredients=[], description=""):
        self.name = str(name)

        if cooking_lvl not in range(1, 6) or not isinstance(cooking_lvl, int):
            raise ValueError("cooking_lvl must be an integer in range 1 to 5")
        self.cooking_lvl =   int(cooking_lvl)

        if not isinstance(cooking_time, int) or int(cooking_time) < 0:
            raise ValueError("cooking_time must be a positive number")
        self.cooking_time = int(cooking_time)

        if not ingredients:
            raise ValueError("ingredients list must be not empty")
        self.ingredients = [str(ing) for ing in ingredients]

        self.description = str(description)

        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("recipe_type must be one of this ['starter', 'lunch', 'dessert']")
        self.recipe_type = recipe_type
    

    def __str__(self):
        return self.name

