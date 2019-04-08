import re
import datetime
import json
import requests
import pandas as pd
from quote_list import *
from write_to_html_file import write_to_html_file

import matplotlib.pyplot as plt
import seaborn as sns


comments_with_futurama = []  # to store post_id's to avoid duplicates
skip_these_subs = ['futurama', 'FuturamaWOTgame',
                   'Futurama_Sleepers', 'unexpectedfuturama']  # Add any subs you want to skip here
# this will be displayed using Pandas
futurama_post_dict = {"search quote": [], "body": [], "subreddit": [], "author": [],
                      "date": []}  # , "link to comment":[] , "post id":[] , "link id":[]
# keeping a running total of all comments found with futurama quotes in quote_list to print to terminal
post_counter = 0

# this just tells me how many of the quotes have been gone through while running to print to terminal
quote_counter = 1
print()

for quote in quote_list:

    # Get all instances of this quote being used on reddit for your desired time period
    url = 'https://api.pushshift.io/reddit/search/comment/?q=' + quote + '&size=1000&after=1d'
    
    r = requests.get(url).json()
    # print('size: ', len(r['data']))
    
    for child in r['data']:

        if (child['subreddit']) in skip_these_subs: continue

        # this will find the quote substring in the string body for each submission found.
        # is here because pushshift.io is dumping all posts that contain all the words in
        # the quote, and not just those with the quote.  eg. if the post has the words
        # planet and express anywhere in them, it is being added. not sure how to search
        # a sub-string using pushshift
        post_body = str(child['body'])  # for clarity
        for q in expanded_quote_list:
            if str(child['id']) in comments_with_futurama: break

            if re.search(q, post_body, re.IGNORECASE):

                # This just gives me updating info on the console as the script is running
                print('Searching quote: ' + str(quote_counter) + '/' + str(len(quote_list)) +
                      '                 Posts found: ' + str(post_counter), end='\r', flush=True)

                # for clarity/readability when appending to dictionary below
                date = datetime.datetime.fromtimestamp(int(child['created_utc']))
                body = str(child['body'])
                subreddit = str(child['subreddit'])
                author = str(child['author'])
                _id = str(child['id'])
                # .replace() removes the 't3_' so that i can create a link to the post
                link_id = str(child['link_id'].replace('t3_', ''))
                body_hyperlink = '<a href="{0}" target="_blank">{1}</a>'.format(
                    'https://www.reddit.com/comments/' + link_id + '/_/' + _id, body)
                # Append data from post to the dictionary
                futurama_post_dict["date"].append(date)
                futurama_post_dict["search quote"].append(quote)
                futurama_post_dict["body"].append(body_hyperlink)
                futurama_post_dict["subreddit"].append(subreddit)
                futurama_post_dict["author"].append(author)

                # add post id to collected comments list to avoid duplicates
                comments_with_futurama.append(_id)
                post_counter += 1
    quote_counter += 1
print()

# display all text in the cells without truncation
pd.set_option('display.max_colwidth', -1)#253 is a good width...-1 is max width
df1 = pd.DataFrame(futurama_post_dict)
df2 = pd.DataFrame(futurama_post_dict)
# this doesnt sort by date(would need to do df = df.sort...) but it does seem to create a df that fits the screen w/o horizontal scrolling
# df.sort_values(by=['date'])
df1.index += 1  # start index at 1
# Save data in a nice format to an html file # If doing weekly batches, change title to reflect that
table_title = 'Reddit\'s Futurama Posts from ' + \
    str(datetime.date.today()) + ' ------ Total Posts Found: ' + str(post_counter)
write_to_html_file(df1, table_title, 'styledfuturamaposts.html')

# TO PRODUCE A BARCHART USING SEABORN AND MATPLOTLIB
quote_count = df1['search quote'].value_counts()#.plot(kind='barh')
fig = sns.barplot(quote_count.index, quote_count.values, alpha=0.8).get_figure()
plt.title('Frequency of futurama quotes')
plt.ylabel('Number of Occurences', fontsize=12)
# plt.xlabel('Quotes Found', fontsize=12)
plt.xticks(rotation=55, ha='right')# angle the x-axis labels and center them under the bar at the last letter of the quote
fig.set_size_inches(25, 9)
# plt.savefig('barGraph.png', bbox_inches='tight')
# plt.yscale('log')# display the y-axis as a logarithmic axis

# # # THIS IS AN ATTEMPT TO ADD VALUES/PERCENTAGES ABOVE THE BARS ON THE GRAPH
# for i in fig.patches:
#     print('in here')
#     fig.text(i.get_x()+.04, i.get_height()+12000, \
#     str(round((i.get_height()), 2)), fontsize=11, color='dimgrey', rotation=45)


fig.savefig('barGraph.png', bbox_inches='tight')


# # TO PRODUCE A PIE GRAPH USING MATPLOTLIB
# quote_count2 = df2['search quote'].value_counts()
# labels = quote_count2.index
# sizes = quote_count2.values
# plt.pie(sizes, 
#         labels=labels,
#         shadow=True,
#         autopct='%1.1f%%')

# plt.axis('equal')
# plt.show()
# # plt.savefig('pieChart.png')

# df2.to_csv('futurama.csv')# save to a csv file so I can play with matplotlib using this data