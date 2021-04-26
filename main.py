#!/usr/bin/python3
import plotly.graph_objects as go
from fruits import append_fruit_data
from helpers import BASE_URL
from helpers import get_frequencies
from helpers import get_category_recipes
from entrees import get_entrees_frequencies
from entrees import sort_meats
from entrees import append_meats_data
from desserts import get_desserts_frequencies
from desserts import sort_desserts
from desserts import append_desserts_data
from nutrition import get_calories_per_serving

monochrome_colors = ['#251616', '#760000', '#C63F3F', '#E28073', '#F1D3CF']
primary_colors = ['#C63F3F', '#F4B436', '#83BFCC', '#455574', '#E2DDDB']

# HODP template
theme_hodp = go.layout.Template(
    layout=go.Layout(
        title={
            'font': {
                'size': 24,
                'family': 'Helvetica',
                'color': monochrome_colors[0]
            },
            'pad': {
                't': 100,
                'r': 0,
                'b': 0,
                'l': 0
            }
        },
        font={
            'size': 18,
            'family': 'Helvetica',
            'color':'#717171'
        },
        xaxis={
            'ticks': 'outside',
            'tickfont': {
                'size': 14,
                'family': 'Helvetica'
            },
            'showticksuffix': 'all',
            'showtickprefix': 'last',
            'showline': True,
            'title': {
                'font': {
                    'size': 18,
                    'family': 'Helvetica'
                },
                'standoff': 20
            },
            'automargin': True
        },
        yaxis={
            'ticks': 'outside',
            'tickfont': {
                'size': 14,
                'family': 'Helvetica'
            },
            'showticksuffix': 'all',
            'showtickprefix': 'last',
            'title': {
                'font': {
                    'size': 18,
                    'family': 'Helvetica'
                },
                'standoff': 20
            },
            'showline': True,
            'automargin': True
        },
        legend={
            'bgcolor': 'rgba(0,0,0,0)',
            'title': {
                'font': {
                    'size': 18,
                    'family': 'Helvetica',
                    'color': monochrome_colors[0]
                }
            },
            'font': {
                'size': 14,
                'family': 'Helvetica'
            },
            'yanchor': 'bottom'
        },
        colorscale={
            'diverging': monochrome_colors
        },
        coloraxis={
            'autocolorscale': True,
            'cauto': True,
            'colorbar': {
                'tickfont': {
                    'size': 14,
                    'family': 'Helvetica'
                },
                'title': {
                    'font': {
                        'size': 18,
                        'family': 'Helvetica'
                    }
                }
            }
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

    append_fruit_data(2019, 12, X_month_year, Y_Bananas, Y_Oranges, Y_Apples,
                      Y_Grapefruit, Y_Salad_Cups, Y_Hand_Fruit)
    for i in range(1, 13):
        append_fruit_data(2020, i, X_month_year, Y_Bananas, Y_Oranges, Y_Apples,
                          Y_Grapefruit, Y_Salad_Cups, Y_Hand_Fruit)
    for i in range(1, 4):
        append_fruit_data(2021, i, X_month_year, Y_Bananas, Y_Oranges, Y_Apples,
                          Y_Grapefruit, Y_Salad_Cups, Y_Hand_Fruit)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=X_month_year,
            y=Y_Bananas,
            name='Bananas',
            mode='lines+markers',
            marker_color=primary_colors[0]
        )
    )

    fig.add_trace(
        go.Scatter(
            x=X_month_year,
            y=Y_Apples,
            name='Apples',
            mode='lines+markers',
            marker_color=monochrome_colors[0]
        )
    )

    fig.add_trace(
        go.Scatter(
            x=X_month_year,
            y=Y_Oranges,
            name='Oranges',
            mode='lines+markers',
            marker_color=monochrome_colors[1]
        )
    )

    fig.add_trace(
        go.Scatter(
            x=X_month_year,
            y=Y_Grapefruit,
            name='Grapefruit',
            mode='lines+markers',
            marker_color=primary_colors[2]
        )
    )

    fig.add_trace(
        go.Scatter(
            x=X_month_year,
            y=Y_Hand_Fruit,
            name='Hand Fruit',
            mode='lines+markers',
            marker_color=monochrome_colors[2]
        )
    )

    fig.add_trace(
        go.Scatter(
            x=X_month_year,
            y=Y_Salad_Cups,
            name='Salad Cups',
            mode='lines+markers',
            marker_color=primary_colors[3]
        )
    )

    fig.update_layout(
        title='Comparison of HUDS\' Fresh Fruit Offerings',
        xaxis={
            'title': {
                'text': 'Month'
            }
        },
        yaxis={
            'title': {
                'text': 'Number of Listings'
            }
        },
        legend={
            'title': {
                'text': 'Groups'
            }
        },
        template=theme_hodp
    )

    fig.show()

def plot_entree_meats():
    X_month_year = []
    Y_Chicken = []
    Y_Beef = []
    Y_Poultry = []
    Y_Shrimp = []
    Y_Turkey = []
    Y_Fish = []
    Y_Sausage = []
    Y_Tofu = []
    Y_Egg = []
    Y_Meatball = []
    Y_Others = []

    append_meats_data(2019, 12, X_month_year, Y_Chicken, Y_Beef, Y_Poultry,
                      Y_Shrimp, Y_Turkey, Y_Fish, Y_Sausage, Y_Tofu, Y_Egg,
                      Y_Meatball, Y_Others)
    for i in range(1, 13):
        append_meats_data(2020, i, X_month_year, Y_Chicken, Y_Beef, Y_Poultry,
                          Y_Shrimp, Y_Turkey, Y_Fish, Y_Sausage, Y_Tofu, Y_Egg,
                          Y_Meatball, Y_Others)
    for i in range(1, 4):
        append_meats_data(2021, i, X_month_year, Y_Chicken, Y_Beef, Y_Poultry,
                          Y_Shrimp, Y_Turkey, Y_Fish, Y_Sausage, Y_Tofu, Y_Egg,
                          Y_Meatball, Y_Others)

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Others,
            name='Others',
            marker_color='#60009F',
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Turkey,
            name='Turkey',
            marker_color='#00A000',
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Tofu,
            name='Tofu',
            marker_color='#2000DF',
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Shrimp,
            name='Shrimp',
            marker_color=monochrome_colors[3],
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Meatball,
            name='Meatball',
            marker_color=monochrome_colors[2],
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Egg,
            name='Egg',
            marker_color=monochrome_colors[1],
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Sausage,
            name='Sausage',
            marker_color=monochrome_colors[0],
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Fish,
            name='Fish',
            marker_color=primary_colors[3],
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Beef,
            name='Beef',
            marker_color=primary_colors[2],
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Poultry,
            name='Poultry',
            marker_color=primary_colors[1],
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Chicken,
            name='Chicken',
            marker_color=primary_colors[0],
        )
    )

    fig.update_layout(
        barmode='stack',
        title='Meat Composition of HUDS Entrees',
        xaxis={
            'title': {
                'text': 'Month'
            }
        },
        yaxis={
            'title': {
                'text': 'Number of Entree Listings'
            }
        },
        legend={
            'title': {
                'text':'Groups'
            }
        },
        template=theme_hodp
    )
    fig.show()

def plot_desserts_types():
    X_month_year = []
    Y_Cookies = []
    Y_Pies = []
    Y_Brownies = []
    Y_Squares = []
    Y_Cakes = []
    Y_Frozen_Yogurt = []
    Y_Soft_Serve_Yogurt = []
    Y_Ice_Cream = []
    Y_Pudding = []
    Y_Fruit = []
    Y_Others = []

    append_desserts_data(2019, 12, X_month_year, Y_Cookies, Y_Pies, Y_Brownies,
                         Y_Squares, Y_Cakes, Y_Frozen_Yogurt, Y_Soft_Serve_Yogurt,
                         Y_Ice_Cream, Y_Pudding, Y_Fruit, Y_Others)
    for i in range(1, 13):
        append_desserts_data(2020, i, X_month_year, Y_Cookies, Y_Pies, Y_Brownies,
                             Y_Squares, Y_Cakes, Y_Frozen_Yogurt, Y_Soft_Serve_Yogurt,
                             Y_Ice_Cream, Y_Pudding, Y_Fruit, Y_Others)
    for i in range(1, 4):
        append_desserts_data(2021, i, X_month_year, Y_Cookies, Y_Pies, Y_Brownies,
                             Y_Squares, Y_Cakes, Y_Frozen_Yogurt, Y_Soft_Serve_Yogurt,
                             Y_Ice_Cream, Y_Pudding, Y_Fruit, Y_Others)

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Others,
            name='Others',
            marker_color='#60009F',
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Fruit,
            name='Fruit',
            marker_color='#00A000',
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Pudding,
            name='Pudding',
            marker_color='#2000DF',
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Ice_Cream,
            name='Ice Cream',
            marker_color=monochrome_colors[3],
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Soft_Serve_Yogurt,
            name='Soft Serve Yogurt',
            marker_color=monochrome_colors[2],
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Frozen_Yogurt,
            name='Frozen Yogurt',
            marker_color=monochrome_colors[1],
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Cakes,
            name='Cakes',
            marker_color=monochrome_colors[0],
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Squares,
            name='Squares',
            marker_color=primary_colors[3],
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Brownies,
            name='Brownies',
            marker_color=primary_colors[2],
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Pies,
            name='Pies',
            marker_color=primary_colors[1],
        )
    )

    fig.add_trace(
        go.Bar(
            x=X_month_year,
            y=Y_Cookies,
            name='Cookies',
            marker_color=primary_colors[0],
        )
    )

    fig.update_layout(
        barmode='stack',
        title='Categorizing HUDS\' Desserts',
        xaxis={
            'title': {
                'text': 'Month'
            }
        },
        yaxis={
            'title': {
                'text': 'Number of Dessert Listings'
            }
        },
        legend={
            'title': {
                'text':'Groups'
            }
        },
        template=theme_hodp
    )
    fig.show()

def plot_cps():
    Y_entrees_cps = []
    Y_breakfast_entrees_cps = []
    Y_ventrees_cps = []
    Y_desserts_cps = []

    get_calories_per_serving(12, Y_entrees_cps)
    get_calories_per_serving(2, Y_breakfast_entrees_cps)
    get_calories_per_serving(13, Y_ventrees_cps)
    get_calories_per_serving(17, Y_desserts_cps)

    fig = go.Figure()
    fig.add_trace(
        go.Box(
            x=Y_entrees_cps,
            marker_color=primary_colors[0],
            name='Entrees',
            boxpoints='outliers'
        )
    )

    fig.add_trace(
        go.Box(
            x=Y_breakfast_entrees_cps,
            marker_color=primary_colors[1],
            name='Breakfast Entrees',
            boxpoints='outliers'
        )
    )

    fig.add_trace(
        go.Box(
            x=Y_ventrees_cps,
            marker_color=primary_colors[2],
            name='Vegetarian Entrees',
            boxpoints='outliers'
        )
    )

    fig.add_trace(
        go.Box(
            x=Y_desserts_cps,
            marker_color = primary_colors[3],
            name='Desserts',
            boxpoints='outliers'
        )
    )

    fig.update_layout(
        title='Calories per Serving of HUDS Entrees and Desserts',
        xaxis=dict(tickmode='linear',
                   tick0=0,
                   dtick=5,
                   title={'text': 'Calories per Ounce or Fluid Ounce'}),
        xaxis_range=[0, 130],
        yaxis={
            'title': {
                'text': 'Food Categories'
            }
        },
        legend={
            'title': {
                'text': 'Groups'
            }
        },
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

    target_categories = [
        #(1, 'Breakfast Meats'),
        #(2, 'Breakfast Entrees'),
        #(3, 'Breakfast Bakery'),
        #(4, 'Breakfast Misc'),
        #(5, 'Breakfast Breads'),
        #(7, 'Today\'s Soup'),
        #(9, 'Brunch'),
        #(10, 'Salad Bar'),
        #(11, 'Sandwich Bar'),
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
    ]

    plot_desserts_types()
    # plot_cps()
