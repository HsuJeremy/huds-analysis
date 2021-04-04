import requests
from helpers import get_frequencies, days_in_month, BASE_URL

# Get fruit frequencies for a single month 
def get_fruit_frequencies(start_year, start_month, location=None):
    fruit_freq = {}
    count = get_frequencies(start_year, start_month, 1, days_in_month(start_year, start_month), [(32, 'Fresh Fruit')])
    num_recipes = len(count.keys())
    ordered_frequencies = count.most_common(num_recipes)
    for (recipe_id, category), occurrences in ordered_frequencies:
        name = requests.get((BASE_URL + '/recipes/' + str(recipe_id))).json()['name']
        fruit_freq[name] = occurrences
    return fruit_freq



def append_fruit_data(start_year, start_month, X_list, Y_b, Y_o, Y_a, Y_g, Y_s, Y_h):
    X_list.append(str(start_month) + "/" + str(start_year))
    fruit_freq = get_fruit_frequencies(start_year, start_month)
    try:
        Y_b.append(fruit_freq['Fruit, Bananas'])
    except:
        Y_b.append(0)
    try:
        Y_o.append(fruit_freq['Fruit, Oranges'])
    except:
        Y_o.append(0)
    try:
        Y_a.append(fruit_freq['Fruit, Local Apples'])
    except:
        Y_a.append(0)
    try:
        Y_g.append(fruit_freq['Fruit, Grapefruit'])
    except:
        Y_g.append(0)
    try:
        Y_s.append(fruit_freq['Fruit Salad Cups'])
    except:
        Y_s.append(0)
    try:
        Y_h.append(fruit_freq['Seasonal Hand Fruit'])
    except:
        Y_h.append(0)