#!/usr/bin/python3
import os
import requests


BASE_URL = 'https://api.cs50.io/dining'

if __name__ == '__main__':
    # Print categories
    categories = requests.get(os.path.join(BASE_URL, 'categories')).json()
    print('CATEGORIES')
    for item in categories:
        print(item['name'])

    # Print locations
    locations = requests.get(os.path.join(BASE_URL, 'locations')).json()
    print('\nLOCATIONS')
    for item in locations:
        print(item['name'])

    # Print Annenberg's breakfast menu for 3/22/2021
    params = {'location': 7, 'date': '2021-03-22', 'meal': 0}
    menu = requests.get(os.path.join(BASE_URL, 'menus'), params).json()
    print('\nANNENBERG BREAKFAST MENU 3/22/2021')
    for item in menu:
        category = requests.get(os.path.join(BASE_URL, 'categories', str(item['category']))).json()
        recipe = requests.get(os.path.join(BASE_URL, 'recipes', str(item['recipe']))).json()
        print('Category: {:<30}   Dish: {}'.format(category['name'], recipe['name']))
