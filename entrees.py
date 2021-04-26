import requests
from helpers import get_frequencies
from helpers import days_in_month
from helpers import BASE_URL

# Get entrees frequencies for a single month
def get_entrees_frequencies(start_year, start_month, location=None):
    entrees_freq = {}
    count = get_frequencies(start_year, start_month, 1,
                            days_in_month(start_year, start_month),
                            [(12, 'Entrees')])
    num_recipes = len(count.keys())
    ordered_frequencies = count.most_common(num_recipes)
    for (recipe_id, _), occurrences in ordered_frequencies:
        url = '{}/recipes/{}'.format(BASE_URL, recipe_id)
        name = requests.get(url).json()['name']
        entrees_freq[name] = occurrences
    return entrees_freq

def sort_meats(start_year, start_month):
    entrees_freq = get_entrees_frequencies(start_year, start_month)
    meat_freq = {
        'Chicken': 0,
        'Beef': 0,
        'Poultry': 0,
        'Shrimp': 0,
        'Turkey': 0,
        'Fish': 0,
        'Sausage': 0,
        'Tofu': 0,
        'Egg': 0,
        'Meatball': 0,
        'Others': 0
    }
    for key, value in entrees_freq.items():
        key_sorted = False
        if 'Chicken' in key:
            meat_freq['Chicken'] = meat_freq['Chicken'] + value
            key_sorted = True
        if 'Beef' in key or 'Steak' in key or 'Sloppy Joes' in key:
            meat_freq['Beef'] = meat_freq['Beef'] + value
            key_sorted = True
        if 'Ham' in key or 'Pork' in key or 'Bacon' in key:
            meat_freq['Poultry'] = meat_freq['Poultry'] + value
            key_sorted = True
        if 'Shrimp' in key:
            meat_freq['Shrimp'] = meat_freq['Shrimp'] + value
            key_sorted = True
        if 'Turkey' in key:
            meat_freq['Turkey'] = meat_freq['Turkey'] + value
            key_sorted = True
        if (
            'Catch' in key
            or 'Cod' in key
            or 'Salmon' in key
            or 'Flounder' in key
            or 'Fish' in key
            or 'FISH' in key
        ):
            meat_freq['Fish'] = meat_freq['Fish'] + value
            key_sorted = True
        if 'Sausage' in key:
            meat_freq['Sausage'] = meat_freq['Sausage'] + value
            key_sorted = True
        if 'Tofu' in key:
            meat_freq['Tofu'] = meat_freq['Tofu'] + value
            key_sorted = True
        if 'Egg' in key:
            meat_freq['Egg'] = meat_freq['Egg'] + value
            key_sorted = True
        if 'Meatball' in key:
            meat_freq['Meatball'] = meat_freq['Meatball'] + value
            key_sorted = True
        if not key_sorted:
            meat_freq['Others'] = meat_freq['Others'] + value
    return meat_freq

def append_meats_data(start_year, start_month, X_list, Y_ch, Y_bf, Y_pl, Y_sh,
                      Y_tk, Y_fs, Y_ss, Y_tf, Y_eg, Y_mt, Y_ot):
    X_list.append(str(start_month) + '/' + str(start_year))
    Y_lists = {
        'Chicken': Y_ch,
        'Beef': Y_bf,
        'Poultry': Y_pl,
        'Shrimp': Y_sh,
        'Turkey': Y_tk,
        'Fish': Y_fs,
        'Sausage': Y_ss,
        'Tofu': Y_tf,
        'Egg': Y_eg,
        'Meatball': Y_mt,
        'Others': Y_ot
    }
    meat_freq = sort_meats(start_year, start_month)
    for key, value in Y_lists.items():
        value.append(meat_freq[key])
