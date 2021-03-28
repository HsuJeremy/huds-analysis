#!/usr/bin/python3
import os
import requests
from collections import Counter


BASE_URL = 'https://api.cs50.io/dining'

# Assume date is valid
def date_to_string(year, month, day):
    year_str = str(year)
    month_str = '0' + str(month) if month < 10 else str(month)
    day_str = '0' + str(day) if day < 10 else str(day)
    return '{}-{}-{}'.format(year_str, month_str, day_str)

# Assume date range spans only one month
def get_frequencies(start_year, start_month, start_day, num_days, categories):
    recipe_ids = []
    ceiling = start_day + num_days
    while start_day < ceiling:
        date_str = date_to_string(start_year, start_month, start_day)
        for category_id, _ in categories:
            params = {'date': date_str, 'category': category_id}
            menu = requests.get(os.path.join(BASE_URL, 'menus'), params).json()
            for item in menu:
                recipe_ids.append((item['recipe'], category_id))
        start_day += 1
    return Counter(recipe_ids)

if __name__ == '__main__':
    target_categories = [
        # (1, 'Breakfast Meats'),
        # (2, 'Breakfast Entrees'),
        # (4, 'Breakfast Misc'),
        (7, 'Today\'s Soup'),
        (9, 'Brunch'),
        (12, 'Entrees'),
        (13, 'Vegetarian Entree'),
        # (14, 'Starch and Potatoes'),
        # (15, 'Vegetables'),
        # (16, 'Sides'),
        # (17, 'Desserts'),
        (26, 'Entree Salads'),
        (59, 'VEGETARIAN ENTREE'),
        (60, 'Entrees'),
        # (65, 'Breakfast'),
        (71, 'Pizza')
    ]

    count = get_frequencies(2020, 3, 1, 14, target_categories)
    num_recipes = len(count.keys())
    ordered_frequencies = count.most_common(num_recipes)
    for (recipe_id, category), occurrences in ordered_frequencies:
        name = requests.get(os.path.join(BASE_URL, 'recipes', str(recipe_id))).json()['name']
        print(name, category, occurrences)
