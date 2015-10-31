# -*- coding: utf-8 -*-
"""
	@
    @Description:   This script generates a graph that shows the
    @               distribution of tweets by date
    @               
    @               
    @Author:        Joe Chen
    @Last modified: 07/09/2015 
"""

import time
import ujson as json
import sys
morepath = ['/Users/zc/Documents/twitter_research/TurkishElection/src/RESTApi', '/Library/Python/2.7/site-packages/mmseg-1.3.0-py2.7-macosx-10.9-intel.egg', '/Library/Python/2.7/site-packages/PyInstaller-2.1-py2.7.egg', '/Library/Python/2.7/site-packages/distribute-0.7.3-py2.7.egg', '/Library/Python/2.7/site-packages/py2app-0.9-py2.7.egg', '/Library/Python/2.7/site-packages/modulegraph-0.12-py2.7.egg', '/Library/Python/2.7/site-packages/altgraph-0.12-py2.7.egg', '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python', '/Library/Python/2.7/site-packages/mechanize-0.2.5-py2.7.egg', '/Library/Python/2.7/site-packages/oauth2-1.5.211-py2.7.egg', '/Library/Python/2.7/site-packages/httplib2-0.9-py2.7.egg', '/usr/local/lib/wxPython-3.0.2.0/lib/python2.7/site-packages', '/usr/local/lib/wxPython-3.0.2.0/lib/python2.7/site-packages/wx-3.0-osx_cocoa', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload', '/Users/zc/Library/Python/2.7/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages', '/usr/local/lib/wxPython-3.0.2.0/lib/python2.7', '/Library/Python/2.7/site-packages']
sys.path += morepath

import pymongo
import datetime 
import itertools
from pymongo import MongoClient
import numpy as np
from matplotlib import pyplot as plt
from sets import Set


withheld = [3149317209, 2438241031, 1455117540, 1468619406, 2269410145, 223401306, 55931558, 2787092860, 3060195898, 773522234, 2873735931, 476129032, 108722820, 1534842866, 321693960, 2721640627, 2907606317, 2293151024, 337634665, 428841793, 496123353, 2882277809, 2282535014, 2225934435, 273648929, 2816108855, 2866130302, 152621713, 2734487861, 3312091571, 414128153, 2965856032, 2971370008, 405387961, 2837399020, 2849619365, 2518761755, 321283148, 435022913, 408618373, 1288644836, 2464744725, 2700939031, 1288647019, 2808943270, 161037892, 383660696, 222564497, 487660641]

def createListFromJson(filename):
	# inputJson=open(filename, "r").read()
	# jsonFields=json.loads(inputJson)
	print "finish loading json data"
	count = 1
	time_list = []

	with open(filename) as f:
		for line in f:
			tweet = json.loads(line)

			if count % 10000 == 0:
				print count
			count += 1

			if tweet[u"lang"] == "ar":
				created_at = tweet[u'created_at']
				#time_list.append(created_at)
				yield(created_at)
	#return time_list


def createList(collection):
	count = 0	             # count total number of tweets
	original = 0
	for tweet in collection.find():
			count += 1
			if (count % 5000 == 0):
				# keep track of how many tweets have been processed
				print count

			created_at =  tweet[u'created_at']
			# try:
			# 	tweet[u'retweeted_status']				
			# except:
			# 	try:
			# 		created_at =  tweet[u'created_at']
			# 		original += 1
			# 	except:
			# 		continue
			yield(created_at)  					# use a generator 

	print "number of original tweets is --> ", original

def formatTime(creat_time, start_time, end_time):
	# only consider tweets before 12/08/2014, data become incomplete after 12/08/2014
	# end_time = datetime.datetime(2099, 12, 8)   
	datelist = []                            	# store datetime objects into a list
	for everytime in creat_time:
		dt = datetime.datetime.strptime(everytime, '%a %b %d %H:%M:%S +0000 %Y')  # format the time
		if dt < end_time and start_time < dt:
			""" 
				Because the event dates are based on HK time,
				if you want to align the timezone to HongKong time, 
				you can change the argument to (hours = 8), 
				GMT/UTC + 08:00 hour
			"""
			datelist.append(dt + datetime.timedelta(hours = 0)) 	
	return datelist

def plotTimeFreq(datelist, filename="../output/timeline.pdf"):
	datelist = sorted(datelist)
	OY = []                # store y values (number of tweets)
	OX = []                # store x values (string of dates )


	newdate =  [list(g) for k, g in itertools.groupby(datelist, key=datetime.datetime.toordinal)]
	for x in xrange(0,len(newdate) ):
		#print len(newdate[x]), newdate[x][0].date()
		OY.append(len(newdate[x]))
		OX.append(str (newdate[x][0].date()) )

	fig = plt.figure()
	plt.ylabel('Number of tweets')                # add titles and label
	plt.xlabel('Date')
	plt.title('Distribution of tweets by day--Turkish Election')
	ind = np.arange(len(OY))

	plt.bar(ind, OY, width = 0.80)
	plt.xticks(ind, OX, rotation='vertical')    		    # add date labels on x-axis


	# store a list of event days
	"""include event dates specified by Prof. Stoll"""
	# event_days = [[2014, 10, 6],[2014, 10, 9],[2014, 10, 13],[2014, 10, 14],[2014, 10, 15],   
	# 			[2014, 10, 17],[2014, 10, 21],[2014, 11, 13],[2014, 11, 15],[2014, 11, 18],
	# 			[2014, 11, 26],[2014, 11, 30],[2014, 12, 1],[2014, 12, 2]]

	count = 0
	colors = "rgrcmykbrgrcmykbrgrcmykb"
	color_index = 0

	# draw each event as a vertical line
	# for day in event_days:
	# 	event_day = datetime.date(day[0], day[1], day[2])
	# 	day_diff = event_day -  first_day       	# find the difference
	# 	plt.axvline(x = day_diff.days + 0.5 ,color=colors[color_index],ls='-', linewidth=4)
	# 	count += 1
	# 	color_index += 1
	
	fig.set_size_inches(80, 20)
	#if filename != None:
	plt.savefig(filename)
	plt.show()

# human_source = [ "Twitter for iPhone", "Twitter for Android", "Twitter for Websites", "Twitter for iPad", "TweetDeck", "Facebook", "Google", "publicize.wp.com", "Twitter for Android Tablets", "www.apple.com", "BlackBerry", "Windows Phone", "Mobile Web", "Twitter for Mac", "tumblr", "instagram", "linkedin"]


def makeplot(collection, filename):
	data = formatTime(createList(collection))
	plotTimeFreq(data, filename = filename)

if __name__ == '__main__':

		start = time.time()
		""" 
			Please change db, collection to the one you want
		"""
		client = MongoClient()                           # connect to the server             
		db = client.turkishElection             				 # choose a database   
		collection = db.timelinewithheld              				 # choose a collection 
		#data = formatTime(createListFromJson("../usual.json"))
		""" CHANGE the end_time to whenever you want"""
		end_time = datetime.datetime(2015, 10, 1)
		start_time = datetime.datetime(2014, 1, 1)
		data = formatTime(createList(), start_time, end_time)
		"""If you want to save the figure, use 
			plotTimeFreq(data, save = True, filename = filename)
		"""
		filename = "TE_timeline_all_tweet_distribution_by_day.pdf"  # optional
		plotTimeFreq(data, save = True, filename = filename)

		end = time.time()
		print end - start

