import requests
from collections import Counter

BASE_URL = 'https://api.cs50.io/dining'

# Assume date is valid
def date_to_string(year, month, day):
    year_str = str(year)
    month_str = '0' + str(month) if month < 10 else str(month)
    day_str = '0' + str(day) if day < 10 else str(day)
    return '{}-{}-{}'.format(year_str, month_str, day_str)

def days_in_month(year, month):
    if month == 2:
        if year % 4 == 0:
            return 29
        else:
            return 28
    if month <= 7:
        if month % 2 == 0 and month != 2:
            return 30
        elif month == 2:
            return 28
        else:
            return 31
    if month > 7 and month % 2 == 0:
        return 31
    else:
        return 30

# Assume date range spans only one month and all other inputs are valid
def get_frequencies(start_year, start_month, start_day, num_days, categories, location=None):
    recipe_ids = []
    ceiling = start_day + num_days
    while start_day < ceiling:
        date_str = date_to_string(start_year, start_month, start_day)

        for category_id, _ in categories:
            params = {'date': date_str, 'category': category_id}
            if location:
                params['location'] = location
            menu = requests.get((BASE_URL + '/menus'), params).json()
            for item in menu:
                recipe_ids.append((item['recipe'], category_id))
        start_day += 1

    return Counter(recipe_ids)