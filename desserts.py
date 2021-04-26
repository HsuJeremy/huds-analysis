import requests
from helpers import get_frequencies
from helpers import days_in_month
from helpers import BASE_URL

# Get entrees frequencies for a single month
def get_desserts_frequencies(start_year, start_month, location=None):
    desserts_freq = {}
    count = get_frequencies(start_year, start_month, 1,
                            days_in_month(start_year, start_month),
                            [(17, 'Desserts')])
    num_recipes = len(count.keys())
    ordered_frequencies = count.most_common(num_recipes)
    for (recipe_id, _), occurrences in ordered_frequencies:
        url = '{}/recipes/{}'.format(BASE_URL, str(recipe_id))
        name = requests.get(url).json()['name']
        desserts_freq[name] = occurrences
    return desserts_freq

def sort_desserts(start_year, start_month):
    desserts_freq = get_desserts_frequencies(start_year, start_month)
    dessert_types = {
        'Cookies': 0,
        'Pies': 0,
        'Brownies': 0,
        'Squares': 0,
        'Cakes': 0,
        'Frozen Yogurt': 0,
        'Soft Serve Yogurt': 0,
        'Ice Cream': 0,
        'Pudding': 0,
        'Fruit': 0,
        'Others': 0
    }
    for key, value in desserts_freq.items():
        key_sorted = False
        if 'Cookie' in key:
            dessert_types['Cookies'] = dessert_types['Cookies'] + value
            key_sorted = True
        if 'Pie' in key:
            dessert_types['Pies'] = dessert_types['Pies'] + value
            key_sorted = True
        if 'Brownie' in key:
            dessert_types['Brownies'] = dessert_types['Brownies'] + value
            key_sorted = True
        if 'Square' in key:
            dessert_types['Squares'] = dessert_types['Squares'] + value
            key_sorted = True
        if 'Cake' in key or 'cake' in key or 'Tiramisu' in key:
            dessert_types['Cakes'] = dessert_types['Cakes'] + value
            key_sorted = True
        if 'Frozen Yogurt' in key:
            dessert_types['Frozen Yogurt'] = dessert_types['Frozen Yogurt'] + value
            key_sorted = True
        if 'Soft Serve Yogurt' in key:
            dessert_types['Soft Serve Yogurt'] = dessert_types['Soft Serve Yogurt'] + value
            key_sorted = True
        if 'Ice Cream' in key:
            dessert_types['Ice Cream'] = dessert_types['Ice Cream'] + value
            key_sorted = True
        if 'Pudding' in key:
            dessert_types['Pudding'] = dessert_types['Pudding'] + value
            key_sorted = True
        if key == 'Pineapple' or key == 'Watermelon':
            dessert_types['Fruit'] = dessert_types['Fruit'] + value
            key_sorted = True
        if not key_sorted:
            dessert_types['Others'] = dessert_types['Others'] + value
    return dessert_types

def append_desserts_data(start_year, start_month, X_list, Y_cook, Y_ps, Y_br,
                         Y_sq, Y_cake, Y_fy, Y_ssy, Y_ic, Y_pd, Y_fr, Y_ot):
    X_list.append(str(start_month) + '/' + str(start_year))
    Y_lists = {
        'Cookies': Y_cook,
        'Pies': Y_ps,
        'Brownies': Y_br,
        'Squares': Y_sq,
        'Cakes': Y_cake,
        'Frozen Yogurt': Y_fy,
        'Soft Serve Yogurt': Y_ssy,
        'Ice Cream': Y_ic,
        'Pudding': Y_pd,
        'Fruit': Y_fr,
        'Others': Y_ot
    }
    desserts_freq = sort_desserts(start_year, start_month)
    for key, value in Y_lists.items():
        value.append(desserts_freq[key])
