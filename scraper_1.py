import requests
from bs4 import BeautifulSoup
url = 'https://twitter.com/cricbuzz'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
tweets = soup.findAll('li', 'js-stream-item')
for item in range(len(soup.find_all('p', 'TweetTextSize'))):
    tweet_text = tweets[item].get_text()
    dt = tweets[item].find('title ', '_timestamp js-short-timestamp')
    print('This was tweeted on : ' + str(dt))
    print("tweeted text: "+str(tweet_text))
