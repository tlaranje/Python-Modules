
def validate_ingredients(ingredients: str) -> str:
    valid_ing = ["fire", "water", "earth", "air"]
    lst_ingredients = ingredients.split()

    if all(item in valid_ing for item in lst_ingredients):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
