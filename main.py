#import re
import datetime
import json
import requests
import pandas as pd
import random
from quote_list import expanded_quote_list, testing_quote_list
from write_to_html_file import write_to_html_file, df_to_html, generate_table, table_link

#import matplotlib.pyplot as plt
#import seaborn as sns

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import cufflinks as cf
from plotly import graph_objs as go
import plotly.offline

cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)

def tryAgain(retries=0):
    if retries > 10: 
        print('failed on: ', quote)
        return
    try:
        r = requests.get(url).json()
    except:
        print('retrying ', quote)
        retries+=1
        tryAgain(retries)
    return r

comments_with_futurama = []  # to store post_id's to avoid duplicates
skip_these_subs = ['futurama', 'FuturamaWOTgame',
                   'Futurama_Sleepers', 'unexpectedfuturama']  # Add any subs you want to skip here
# this will be displayed using Pandas
futurama_post_dict = {"search quote": [], "quote hyperlink": [], "body": [], "subreddit": [], "author": [],
                      "date": []}  # , "link to comment":[] , "post id":[] , "link id":[]

#post_data = {} # may use this to unnest the loops below... store the data from the api search as {quote: r} and then use that data for the next loop..

# keeping a running total of all comments found with futurama quotes in quote_list to print to terminal
post_counter = 0

# this just tells me how many of the quotes have been gone through while running to print to terminal
quote_counter = 1
print()

for quote in expanded_quote_list: # this should go back to 'in expanded_quote_list:'

    # This just gives me updating info on the console as the script is running
    print('Searching quote: ' + str(quote_counter) + '/' + str(len(expanded_quote_list)) +
            '                 Posts found: ' + str(post_counter), end='\r', flush=True)

    quote_counter += 1


    ###  THIS IS WHERE MY MAJOR SLOWDOWN OCCURS...
    # Get all instances of this quote being used on reddit for your desired time period
    url = 'https://api.pushshift.io/reddit/search/comment/?q="' +  quote + '"&size=1000&after=1d'

    try:
        r = requests.get(url).json()
    except:
        r = tryAgain()


    for child in r['data']:

        if (child['subreddit']) in skip_these_subs: continue

        # post_body = str(child['body'])  # for clarity

        if str(child['id']) in comments_with_futurama: continue #break


        # for clarity/readability when appending to dictionary below
        date = datetime.datetime.fromtimestamp(int(child['created_utc']))
        body = str(child['body'])
        subreddit = str(child['subreddit'])
        author = str(child['author'])
        _id = str(child['id'])
        # .replace() removes the 't3_' so that i can create a link to the post
        link_id = str(child['link_id'].replace('t3_', ''))
        body_hyperlink = '<a href="{0}" target="_blank">{1}</a>'.format(
            'https://www.reddit.com/comments/' + link_id + '/_/' + _id + '/', body)

        quote_hyperlink = '<a href="{0}" target="_blank">{1}</a>'.format(
            'https://morbotron.com/?q=' + quote, quote)

        futurama_post_dict['quote hyperlink'].append(quote_hyperlink)
        # Append data from post to the dictionary   
        futurama_post_dict["search quote"].append(quote)
        futurama_post_dict["body"].append(body_hyperlink)
        futurama_post_dict["subreddit"].append(subreddit)
        futurama_post_dict["author"].append(author)
        futurama_post_dict["date"].append(date)


        # add post id to collected comments list to avoid duplicates
        comments_with_futurama.append(_id)
        post_counter += 1



df = pd.DataFrame(futurama_post_dict)
bar_series = df['quote hyperlink'].value_counts()
pie_series = df['search quote'].value_counts()
df = df.drop(columns=['search quote'])
df.index += 1


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = 'Finglonger'

bargraph = bar_series.iplot(kind='bar', 
                    xaxis_tickangle=35,
                    theme='solar', 
                    color= '#37db8b', #13B584, #37db8b,  #70E3A0 ##colorscale
                    title=str(post_counter) + ' Futurama Quotes from ' + str(datetime.date.today()) + ' -- Click on a quote for more info',
                    yTitle='Quote Count', 
                    filename='cufflinks/categorical-bar-chart',
                    asFigure=True)
bargraph['layout']['xaxis1']['automargin'] = True



colors = ['#dfe442', '#267baa', '#163542', '#17617c', '#174b5f', '#F5A81A', 
          '#0f9b66', '#605d39', '#37db8b', '#496c76', '#ec0701',
          '#863d65', '#E27202', '#704267', '#AAC5DA', '#FE5552', '#FD91AB']
random.shuffle(colors)
labels, values = zip(*pie_series.items())
piechart = go.Figure(data = [go.Pie(
                    labels=labels,
                    values=values,
                    hole=.3,
                    textposition='inside',
                    marker=dict(colors=colors, line=dict(color='#000000', width=1)),
                    )])
piechart['layout']['paper_bgcolor'] = 'rgba(0,0,0,0)'
piechart['layout']['title'] = 'Hover for details -- select boxes on right to compare'


# scatterplot = df.iplot(kind='scatter', 
#                     mode='markers', 
#                     x='search quote', 
#                     y='subreddit', 
#                     filename='cufflinks/simple-scatter',
#                     size='pop',
#                     text='search quote',
#                     asFigure=True)


app.layout = html.Div([ #style={'background-image': 'url("/assets/planet-express-logo.jpg")'},
    #Header
    html.Div([
        html.H1('The Finglonger \n', style={'text-align': 'center'}),
        # Make the icon clickable
        # html.H1(
        #     html.A([
        #         html.Img(
        #             src=app.get_asset_url('Bender.ico'),
        #             style={
        #                 'float': 'right',
        #                 'height': '100px',
        #                 'width': '100px',
        #                 'position': 'relative',
        #                 'padding-top': 0,
        #                 'padding-right': 0})
        #     ])),
        html.H5('Good News Everyone!!', style={'text-align': 'center'}),
        html.Div('Drag and select any part of the graph to zoom in and inspect.  Double click graph to reset.')
    ], className = "row"),
    #Charts/Graphs
    html.Div([
        html.Div([            
            dcc.Graph(id='bar_chart', style={'height': '600px'}, figure = bargraph)
        ]),#, className = "fourteen columns"
    ], className="row"), 

    html.Div([
        html.Div([            
            dcc.Graph(id='pie_chart',  figure = piechart) #style={'height': '600px'},
        ]),  #     , className = "eleven columns"
    ], className="row"),

    # html.Div([
    #     # data table
    #     html.Div([

    #         dash_table.DataTable(
    #             id='Reddit Posts',
    #             columns = [{'name': i, 'id': i} for i in df.columns],
    #             data = df.to_dict('records'),
    #             style_data={
    #                 'whiteSpace': 'normal',
    #                 'height': 'auto'
    #             },
    #             # style_table={
    #             #     'whiteSpace': 'normal',
    #             #     'height': 'auto', #'600px'
    #             #     # 'overflow': 'scroll'
    #             # },
    #             style_header={
    #                 'backgroundColor': 'rgb(30,30,30)',
    #                 'fontWeight': 'bold'
    #             },
    #             style_cell={
    #                 'textAlign': 'left',
    #                 'backgroundColor': 'rgb(50, 50, 50)',
    #                 'color': 'white'
    #             },
    #             style_cell_conditional=[
    #                 {
    #                     'if': {'column_id': 'Region'},
    #                     'textAlign': 'left'
    #                 }
    #             ],
    #             sort_action='native',
    #             # style_data_conditional=[
    #             #     {
    #             #         'if': {'row_index': 'odd'},
    #             #         'backgroundColor': 'rgb(248, 248, 248)'
    #             #     }
    #             # ],
    #             # row_selectable='multi',
    #             # selected_rows=[0],
    #             # fixed_rows={'headers': True, 'data': 0},
    #             # style_cell_conditional=[
    #             #     {'if': {'column_id': 'search quote'}, 'width': '60px'},
    #             # ],

    #         )
    #     ]),#, className='six columns'
    # ]), #, className = 'row'

    # html.Div(children=[
    #     table_link(df, 'body')
    #     # generate_table(df)
    # ]),

    html.Div([
        html.Iframe(height='800px',
                    width= '100%',
                    srcDoc= df_to_html(df)
        ),
    ]),


    # html.Div([            
    #         dcc.Graph(id='scatterplot', figure = scatterplot)
    #     ], className = "seven columns")

], style={'backgroundColor': '#0091C7'} )  # #70E3A0                  

if __name__ == '__main__':
    app.run_server(debug=True)