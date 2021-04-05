import requests
from collections import Counter

BASE_URL = 'https://api.cs50.io/dining'

categories = [
  (1, "Breakfast Meats"), 
  (2, "Breakfast Entrees"),
  (3, "Breakfast Bakery"),
  (4, "Breakfast Misc"),
  (5, "Breakfast Breads"),
  (7, "Today's Soup"),
  (9, "Brunch"),
  (10, "Salad Bar"),
  (11, "Sandwich Bar"),
  (12, "Entrees"),
  (13, "Vegetarian Entree"),
  (14, "Starch And Potatoes"),
  (15, "Vegetables"),
  (16, "Sides"),
  (17, "Desserts"),
  (18, "Bread, Rolls, Misc Bakery"),
  (19, "From The Grill"),
  (20, "Plant Protein"),
  (21, "Basic Food Table"),
  (22, "Brown Rice Station"),
  (23, "Build Your Own"),
  (24, "Special Bars Board Menu"),
  (25, "Culinary Display"),
  (26, "Entree Salads"),
  (27, "In Addition at Annenberg"),
  (28, "Bistro Bowl"),
  (29, "Side Salads"),
  (31, "Chefs Choice"),
  (32, "Fresh Fruit"),
  (33, "Sandwich Selections"),
  (34, "Vegetarian Sandwich Selections"),
  (36, "Extras"),
  (37, "Bread Choices"),
  (40, "Festive Meals"),
  (42, "Fly-By"),
  (43, "Fly-By Sandwiches and Salads"),
  (45, "Chili Bar"),
  (46, "Whole Grain Pasta Bar"),
  (51, "CR Purchased Bottled Beverages"),
  (52, "CR Baked Goods/Desserts"),
  (53, "CR Snacks/Candy"),
  (54, "Daily Bowl"),
  (55, "International Cuisine"),
  (58, "Deli Sandwiches"),
  (59, "VEGETARIAN ENTREE"),
  (60, "Entrees"),
  (61, "Starch and Vegetable Selection"),
  (62, "Daily Soups"),
  (63, "CR Beverages Prepared"),
  (64, "Salad Bar"),
  (65, "Breakfast"),
  (66, "Misc"),
  (67, "Grains"),
  (68, "From the Grill"),
  (71, "Pizza"),
  (72, "Asian Station"),
  (73, "CR Other Resale Items"),
  (74, "CR Salty Snacks"),
  (75, "Odwalla Juices"),
  (77, "Cereals"),
  (78, "Bagels"),
  (80, "PANINIS"),
  (81, "Cheese"),
  (83, "Yogurts, Jams and Spreads"),
  (84, "Dressings"),
  (85, "Beverages"),
  (87, "Bag Meal Breakfast Options"),
  (88, "Heart of the Plate"),
  (89, "Special Bar"),
  (90, "Brain Break"),
  (91, "Bag Meal Specialty Sandwiches"),
  (92, "Bag Meal Salads"),
  (93, "Bag Meal Build Your Own"),
  (94, "Bag Meal Bread Choices"),
  (95, "Bag Meal Cheese Choices"),
  (96, "Bagged Meal Sides"),
  (97, "Bagged Meal Condiments")
]

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