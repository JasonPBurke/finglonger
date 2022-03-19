import aiohttp
import asyncio
import datetime
# import json
import pandas as pd
import random
from quote_list import quote_list
from write_to_html_file import df_to_html
import dash
import dash_core_components as dcc
import dash_html_components as html
import cufflinks as cf
from plotly import graph_objs as go
# import plotly.offline
import re
from pprint import pprint


cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)

futurama_post_dict = {
    "search quote": [],
    "quote hyperlink": [],
    "body": [],
    "subreddit": [],
    "author": [],
    "date": []
}  # "link to comment":[] , "post id":[] , "link id":[]

post_counter = 0


async def fetch(session, url):
    data = None
    while data is None:
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                data = await response.json()
        except aiohttp.ClientError:
            print(response.status)
            # print(response.status, url)
            await asyncio.sleep(1)
    return data


def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


async def gather():
    comments_with_futurama = []  # to store post_id's to avoid duplicates
    skip_these_subs = [
        'futurama',
        'FuturamaWOTgame',
        'Futurama_Sleepers',
        'FuturamaSleepers',
        'unexpectedfuturama']

    global post_counter
    sub_quote_list = split(quote_list, 42)
    sub_quote_list.append(['futurama'])
    for lst in sub_quote_list:
        quote_batch = [f'"{i}"' for i in lst]
        batch_string = '|'.join(quote_batch)
        tasks = []
        async with aiohttp.ClientSession() as session:
            url = 'https://beta.pushshift.io/reddit/search/comments/?q=' + \
                batch_string + '&limit=1000&smartsince=1d'
            tasks.append(fetch(session, url))
            r = await asyncio.gather(*tasks)

            for child in r[0]['data']:
                # pprint(child)
                # print()

                if (child['subreddit']) in skip_these_subs:
                    continue
                if str(child['id']) in comments_with_futurama:
                    continue

                for q in lst:
                    if re.sub('[^A-Za-z0-9]+', ' ', q.lower()) in re.sub('[^A-Za-z0-9]+', ' ', child['body'].lower()):
                        quote = q
                        break

                # for clarity/readability when appending to dictionary below
                date = datetime.datetime.fromtimestamp(
                    int(child['created_utc']))
                body = str(child['body'])
                subreddit = str(child['subreddit'])
                author = str(child['author'])
                _id = str(child['id'])

                # .replace() removes the 't3_' so that i can create a link to the post
                # link_id = str(child['link_id']).replace('t3_', ''))
                # body_hyperlink = '<a href="{0}" target="_blank">{1}</a>'.format(
                #     'https://www.reddit.com/comments/' + link_id + '/_/' + _id + '/', body)

                body_hyperlink = '<a href="{0}" target="_blank">{1}</a>'.format(
                    'https://www.reddit.com' + str(child['permalink']), body)
                quote_hyperlink = '<a href="{0}" target="_blank">{1}</a>'.format(
                    'https://morbotron.com/?q=' + quote, quote)

                # Append data from post to the dictionary
                futurama_post_dict['quote hyperlink'].append(quote_hyperlink)
                futurama_post_dict["search quote"].append(quote)
                futurama_post_dict["body"].append(body_hyperlink)
                futurama_post_dict["subreddit"].append(subreddit)
                futurama_post_dict["author"].append(author)
                futurama_post_dict["date"].append(date)

                # add body_sha1 to collected comments list to avoid duplicates
                comments_with_futurama.append(child['id'])
                post_counter += 1

loop = asyncio.get_event_loop()
loop.run_until_complete(gather())

df = pd.DataFrame(futurama_post_dict)
df.sort_values(by=['search quote'.lower(), 'date'], inplace=True)
df = df.reset_index()
bar_series = df['quote hyperlink'].value_counts()
pie_series = df['search quote'].value_counts()
df = df.drop(columns=['search quote', 'index'])
df.index += 1

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = 'Finglonger'

bargraph = bar_series.iplot(kind='bar',
                            xaxis_tickangle=35,
                            xaxis_automargin=True,
                            theme='solar',
                            color='#37db8b',  # 13B584, #37db8b,  #70E3A0 ##colorscale
                            # title=dict(text=str(post_counter) + ' Futurama Quotes from ' + str(datetime.date.today()) + ' -- Click on a quote for more info',
                            title=dict(text=str(post_counter) + ' Futurama refrences in the last day -- Click on a quote for more info',
                                       x=0.5, xanchor='center', y=0.95, yanchor='top'),
                            yTitle='Quote Count',
                            filename='cufflinks/categorical-bar-chart',
                            asFigure=True)
bargraph['layout']['hovermode'] = 'x'


colors = ['#863d65', '#E27202', '#ec0701', '#AAC5DA',
          '#FE5552', '#FD91AB', '#37db8b', '#496c76',
          '#267baa', '#174b5f', '#F5A81A', '#163542', ]
# '#163542', '#17617c','#0f9b66', '#605d39', '#704267', ]
random.shuffle(colors)
labels, values = zip(*pie_series.items())
piechart = go.Figure(data=[go.Pie(
    labels=labels,
    values=values,
    hole=.3,
    textposition='inside',
    marker=dict(colors=colors, line=dict(color='#000000', width=.5)),
)])
piechart['layout']['paper_bgcolor'] = 'rgba(0,0,0,0)'
piechart['layout']['title'] = dict(text='Hover for details -- select boxes on right to compare',
                                   x=0.5, xanchor='center', y=0.95, yanchor='top')


app.layout = html.Div([
    # Header
    html.Div([
        html.H1('The Finglonger \n', style={'text-align': 'center'}),
        html.H5('Good News Everyone!!', style={'text-align': 'center'}),
        html.Div(
            'Drag and select any part of the graph to zoom in and inspect.  Double click graph to reset.')
    ], className="row"),
    # Charts/Graphs
    html.Div([
        html.Div([
            dcc.Graph(id='bar_chart', style={
                      'height': '650px'}, figure=bargraph)
        ]),  # , className = "fourteen columns"
    ], className="row"),

    html.Div([
        html.Div([
            dcc.Graph(id='pie_chart',  figure=piechart)
        ]),  # , className = "eleven columns"
    ], className="row"),

    html.Div([
        html.Iframe(height='800px',
                    width='100%',
                    srcDoc=df_to_html(df)
                    ),
    ]),
], style={'backgroundColor': '#0091C7'})  # #70E3A0


if __name__ == '__main__':

    app.run_server(debug=False)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
