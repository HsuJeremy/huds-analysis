#!/usr/bin/python3
import os
import requests
import plotly.graph_objects as go
from collections import Counter
from fruits import append_fruit_data


monochrome_colors = ['#251616', '#760000', '#C63F3F', '#E28073', '#F1D3CF']
primary_colors = ['#C63F3F', '#F4B436', '#83BFCC', '#455574', '#E2DDDB']

# HODP template
theme_hodp = go.layout.Template(
    layout=go.Layout(
        title = {'font':{'size':24, 'family':"Helvetica", 'color':monochrome_colors[0]}, 'pad':{'t':100, 'r':0, 'b':0, 'l':0}},
        font = {'size':18, 'family':'Helvetica', 'color':'#717171'},
        xaxis = {'ticks': "outside",
                'tickfont': {'size': 14, 'family':"Helvetica"},
                'showticksuffix': 'all',
                'showtickprefix': 'last',
                'showline': True,
                'title':{'font':{'size':18, 'family':'Helvetica'}, 'standoff':20},
                'automargin': True
                },
        yaxis = {'ticks': "outside",
                'tickfont': {'size': 14, 'family':"Helvetica"},
                'showticksuffix': 'all',
                'showtickprefix': 'last',
                'title':{'font':{'size':18, 'family':'Helvetica'}, 'standoff':20},
                'showline': True,
                'automargin': True
                },
        legend = {'bgcolor':'rgba(0,0,0,0)', 
                'title':{'font':{'size':18, 'family':"Helvetica", 'color':monochrome_colors[0]}}, 
                'font':{'size':14, 'family':"Helvetica"}, 
                'yanchor':'bottom'
                },
        colorscale = {'diverging':monochrome_colors},
        coloraxis = {'autocolorscale':True, 
                'cauto':True, 
                'colorbar':{'tickfont':{'size':14,'family':'Helvetica'}, 'title':{'font':{'size':18, 'family':'Helvetica'}}},
                }
    )
)

def plot_fruits():
    
    X_month_year = []
    Y_Bananas = []
    Y_Oranges = []
    Y_Apples = []
    Y_Grapefruit = []
    Y_Salad_Cups = []
    Y_Hand_Fruit = []

    append_fruit_data(2019, 12, X_month_year, Y_Bananas, Y_Oranges, Y_Apples, Y_Grapefruit, Y_Salad_Cups, Y_Hand_Fruit)
    X_month_year.append("12/2019")
    for i in range(1, 13):
        append_fruit_data(2020, i, X_month_year, Y_Bananas, Y_Oranges, Y_Apples, Y_Grapefruit, Y_Salad_Cups, Y_Hand_Fruit)
    for i in range(1, 4):
        append_fruit_data(2021, i, X_month_year, Y_Bananas, Y_Oranges, Y_Apples, Y_Grapefruit, Y_Salad_Cups, Y_Hand_Fruit)
    
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=X_month_year,
        y=Y_Bananas,
        name='Bananas',
        mode='lines+markers',
        marker_color=primary_colors[0]
    ))

    fig.add_trace(go.Scatter(
        x=X_month_year,
        y=Y_Apples,
        name='Apples',
        mode='lines+markers',
        marker_color=monochrome_colors[0]
    ))

    fig.add_trace(go.Scatter(
        x=X_month_year,
        y=Y_Oranges,
        name='Oranges',
        mode='lines+markers',
        marker_color=monochrome_colors[1]
    ))

    fig.add_trace(go.Scatter(
        x=X_month_year,
        y=Y_Grapefruit,
        name='Grapefruit',
        mode='lines+markers',
        marker_color=primary_colors[2]
    ))

    fig.add_trace(go.Scatter(
        x=X_month_year,
        y=Y_Hand_Fruit,
        name='Hand Fruit',
        mode='lines+markers',
        marker_color=monochrome_colors[2]
    ))

    fig.add_trace(go.Scatter(
        x=X_month_year,
        y=Y_Salad_Cups,
        name='Salad Cups',
        mode='lines+markers',
        marker_color=primary_colors[3]
    ))

    fig.update_layout(
        title="Comparison of HUDS' Fresh Fruit Offerings", 
        xaxis={'title':{'text':'Month'}},
        yaxis={'title':{'text':'Number of Listings'}},
        legend={'title':{'text':'Groups'}},
        template=theme_hodp
    )
    
    fig.show()

if __name__ == '__main__':
    # Location IDs
    # 3: Cronkhite Dining Room
    # 4: Dudley Cafe
    # 5: Cabot and Pforzheimer House
    # 7: Dunster and Mather House
    # 8: Quincy House
    # 9: Adams House
    # 14: Eliot and Kirkland House
    # 15: Lowell and Winthrop House
    # 16: Leverett House
    # 27: Sebastian's Cafe
    # 29: Fly-By
    # 30: Annenberg Hall
    # 38: Currier House
    # 54: Northwest Cafe

    #target_categories = [
        #(1, 'Breakfast Meats'),
        #(2, 'Breakfast Entrees'),
        #(4, 'Breakfast Misc'),
        #(7, 'Today\'s Soup'),
        #(9, 'Brunch'),
        #(12, 'Entrees'),
        #(13, 'Vegetarian Entree'),
        #(14, 'Starch and Potatoes'),
        #(15, 'Vegetables'),
        #(16, 'Sides'),
        #(17, 'Desserts'),
        #(26, 'Entree Salads'),
        #(32, 'Fresh Fruit'),
        #(59, 'VEGETARIAN ENTREE'),
        #(60, 'Entrees'),
        #(65, 'Breakfast'),
        #(71, 'Pizza')
    #]
    
    #count = get_frequencies(2020, 8, 1, 31, target_categories)
    #num_recipes = len(count.keys())
    #ordered_frequencies = count.most_common(num_recipes)
    #for (recipe_id, category), occurrences in ordered_frequencies:
        #name = requests.get((BASE_URL + '/recipes/' + str(recipe_id))).json()['name']
        #print(name, category, occurrences)
    plot_fruits()

            
    
