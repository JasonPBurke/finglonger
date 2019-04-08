# finglonger
A Program that searches reddit for quotes from the TV show Futurama.  Outputs: HTML file and bar graph.

This prorgram uses a self curated list of Futurama quotes and searches all reddit posts in a pre-defined time frame
for posts that contain one of the listed quotes.  This time frame can be adjusted, and the quote list can be expanded
to suit the needs of the user running the program.  This will output an HTML file that includes the full reddit comment
that the searched quote was found in, a link to the quote in reddit, the subreddit that the comment was found in, the
reddit username that posted the comment, and the time/date the comment was made.  This was made out of curiosity after
seeing many Futurama quotes and wondering just how many there were per day/week/month. (300-500 quotes found per day!)
This will also output a bargraph showing a visual representation of the frequency of each quote.

This program could easily be modified to search for any quote/name that the user wanted to research and is in no way
limited to Futurama quotes.

Resources used: pushshift, requests, pandas, matplotlib, seaborn
