from bs4 import BeautifulSoup
import urllib2
import random
from textblob import TextBlob

# get the soup
url = "https://newyork.craigslist.org/search/mis"
f = urllib2.urlopen(url)
soup = BeautifulSoup(f, 'html.parser')

# get the titles of each missed connection on the first page
titles = soup.select("a.result-title")

# instantiate an empty list
title_list = []

# for each title, strip it and append to empty list
for title in titles:
	scraped_title = title.text.strip()
	title_list.append(scraped_title)


# create a TextBlob out of the list as an entire string
blob = TextBlob(str(title_list))

#create new noun list
nouns = []

# for each noun phrase in a title, take phrases and add to a new list
for noun in blob.noun_phrases:
	nouns.append(noun)


# choose three random noun phrases for a card
card1 = random.choice(nouns)
card2 = random.choice(nouns)
card3 = random.choice(nouns)

# print the cards
print "card one = " + card1
print "card two = " + card2
print "card three = " + card3

