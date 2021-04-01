from datetime import datetime
from recipe import Recipe



class Book:
    def __init__(self, name) -> None:
        self.name = str(name)
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {
            'starter': [],
            'lunch': [],
            'dessert': []
        }
    
    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for key in self.recipes_list.keys():
            for recipe in self.recipes_list.get(key):
                if recipe.name == name:
                    for k in recipe.__dict__.keys():
                        print(f"{k}: {recipe.__dict__.get(k)}")
                    return recipe


    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        recipe_list = []
        for recipe in self.recipes_list.get(recipe_type):
            recipe_list.append(recipe.name)
        return recipe_list


    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print("The arg passed in add_recipe is not a Recipe")
            return
        self.recipes_list.get(recipe.recipe_type).append(recipe)
        self.last_update = datetime.now()