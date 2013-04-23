import feedparser

rss_link = raw_input('Please enter rss feed url: ')

feed = feedparser.parse(rss_link)

for i in feed['items']:
    print 'Tilte: ', i['title'], '\t (published on: ', i['published'], ')\n'
    print i['summary'], '\n', 'Furthure reading: ', i['link'], '\n\n'
