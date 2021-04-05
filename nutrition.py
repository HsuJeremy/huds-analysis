import requests
from helpers import get_category_recipes, BASE_URL

def get_calories_per_serving(category_id, Y_cps):
    recipe_ids = get_category_recipes(category_id)
    non_oz_serving = 0
    for recipe_id in recipe_ids:
        calories = requests.get(BASE_URL + '/recipes/' + str(recipe_id)).json()["calories"]
        serving_size = requests.get(BASE_URL + '/recipes/' + str(recipe_id)).json()["serving_size"]
        serving_size = serving_size.replace('fl. oz', '')
        serving_size = serving_size.replace('oz', '')
        serving_size = serving_size.replace(' ', '')
        try: 
            Y_cps.append(calories * 1.00 / int(serving_size))
        except:
            non_oz_serving = non_oz_serving + 1
