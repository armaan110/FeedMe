import csv
import json
import urllib2
import time
import operator
from collections import OrderedDict

inputFile = 'restaurantList.txt'
outputFile = 'restaurantWeek.csv'
oauth_token = 'putYourTokenHerePls'
foursquareApiUrl = 'https://api.foursquare.com/v2/venues/explore?near=New%20York&query=FeedMe&oauth_token=ThisIsMyToken&v=20160204'

foursquareApiUrl = foursquareApiUrl.replace('ThisIsMyToken', oauth_token)

with open(inputFile) as f:
    content = f.readlines()

content = [x.strip('\n') for x in content]
dictionary = {}

for x in content:
	try:
		urlToOpen = foursquareApiUrl.replace('FeedMe', x.replace(' ','%20'))
		data = json.load(urllib2.urlopen(urlToOpen))
		rating = data['response']['groups'][0]['items'][0]['venue']['rating']
	except:
		rating = 0
	dictionary[x] = rating
	time.sleep(1) #api rate limiter

dictionary = OrderedDict(sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True))

w = csv.writer(open(outputFile, "w"))
for key, val in dictionary.items():
    w.writerow([key, val])