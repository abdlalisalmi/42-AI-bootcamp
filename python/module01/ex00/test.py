from recipe import Recipe
from book import Book
import time




recipe = Recipe(name="cake", cooking_lvl=2, cooking_time=15, recipe_type="lunch", ingredients=["xasxds", 123])
print(str(recipe))


book = Book("book")
print("Book creation date:", book.creation_date)
print("Book last update:", book.last_update)
print("Adding recipe...")
time.sleep(3)
book.add_recipe("recipef")

print("Book last update:", book.last_update)

print("\nGet recipe by name: ")
book.get_recipe_by_name("cake")

print("\nGet recipes by type: ")
print(book.get_recipes_by_types("lunch"))