import os
from pathlib import Path

recipes = Path("Recipes")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress ENTER to continue...")


def recipe_count():
    return sum(1 for f in recipes.rglob("*.txt") if f.is_file())


def category():
    folders = [f for f in recipes.iterdir() if f.is_dir()]

    for i, f in enumerate(folders, 1):
        print(f"{i}. {f.name}")

    while True:
        election = input("\nWrite the name of a category: ")
        check = recipes / election
        if check.exists() and check.is_dir():
            return election
        print("This category doesn't exist")


def create_category():
    cat_name = input("\nWrite the name of the category: ")
    folder = recipes / cat_name

    if not folder.exists():
        folder.mkdir()
        print("Category created successfully")
    else:
        print("This category already exists")


def delete_category():
    cat = category()
    folder = recipes / cat

    if folder.exists():
        for file in folder.glob("*"):
            file.unlink()
        folder.rmdir()
        print("Category deleted")
    else:
        print("Category does not exist")


def recipetext(cat):
    files = list((recipes / cat).glob("*.txt"))

    for i, f in enumerate(files, 1):
        print(f"{i}. {f.stem}")

    election = input("\nWrite the name of the recipe: ")
    return cat, election


def open_recipe(cat, name):
    file = recipes / cat / (name + ".txt")

    if file.exists():
        with file.open("r", encoding="utf-8") as f:
            print("\n--- RECIPE CONTENT ---")
            print(f.read())
    else:
        print("Recipe not found")


def create_recipe(cat):
    file_name = input("Write the name of the recipe: ")
    file = recipes / cat / (file_name + ".txt")

    if not file.exists():
        text = input("Write the recipe content: ")
        with file.open("w", encoding="utf-8") as f:
            f.write(text)
        print("Recipe created")
    else:
        print("This file already exists")


def delete_recipe():
    cat = category()
    cat_path = recipes / cat

    files = list(cat_path.glob("*.txt"))

    for i, f in enumerate(files, 1):
        print(f"{i}. {f.stem}")

    name = input("Write the name of the recipe to delete: ")
    file = cat_path / (name + ".txt")

    if file.exists():
        file.unlink()
        print("Recipe deleted")
    else:
        print("Recipe not found")


print("Welcome to the recipe administrator")
print(f"The route is: {recipes}")
print(f"The total number of recipes is: {recipe_count()}")

option = 0

while option != "6":
    print("""
Option 1: Read a recipe
Option 2: Create a recipe
Option 3: Create a category
Option 4: Delete a recipe
Option 5: Delete a category
Option 6: Exit
""")

    option = input("Choose a number: ")

    match option:
        case "1":
            t = category()
            t, n = recipetext(t)
            open_recipe(t, n)
            pause()
            clear()

        case "2":
            create_recipe(category())
            pause()
            clear()

        case "3":
            create_category()
            pause()
            clear()

        case "4":
            delete_recipe()
            pause()
            clear()

        case "5":
            delete_category()
            pause()
            clear()

        case "6":
            print("Goodbye!")

        case _:
            print("Please choose a number between 1 and 6")