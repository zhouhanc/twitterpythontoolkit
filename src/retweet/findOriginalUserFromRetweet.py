"""
	@
	@Description:   This python script retrieves all original users from all retweets 
	@ 				in a database              
	@
	@Author:        Joe Chen
	@Last modified: 10/05/2015 
"""
import pprint
import time
import ujson as json
import os
import pymongo
import datetime 
import itertools
from pymongo import MongoClient
from collections import defaultdict
from sets import Set

#withheld = [3149317209, 2438241031, 1455117540, 1468619406, 2269410145, 223401306, 55931558, 2787092860, 3060195898, 773522234, 2873735931, 476129032, 108722820, 1534842866, 321693960, 2721640627, 2907606317, 2293151024, 337634665, 428841793, 496123353, 2882277809, 2282535014, 2225934435, 273648929, 2816108855, 2866130302, 152621713, 2734487861, 3312091571, 414128153, 2965856032, 2971370008, 405387961, 2837399020, 2849619365, 2518761755, 321283148, 435022913, 408618373, 1288644836, 2464744725, 2700939031, 1288647019, 2808943270, 161037892, 383660696, 222564497, 487660641]

def findoriginal(collection, filename="../output/OriginalUserFromRetweets.txt"):
	count = 0
	numretweet = 0
	originaluser = Set([])
	for tweet in collection.find():

		#if tweet[u'user'][u'id'] in withheld:
			count += 1
			if count % 5000 == 0:
				print "read " + str(count) + " tweets"

			if u"retweeted_status" in tweet:
				numretweet += 1
				originaluser.add(tweet[u"retweeted_status"][u'user'][u'id'])

	print "number of retweet --> ", numretweet
	print "number of original users -->", len(originaluser)

	print "start writing to file----"
	f = open(filename, "w")
	for user in originaluser:
		f.write(str(user) + "\n")
	f.close()
	print "finish writing to file----"

if __name__ == '__main__':
	# Connect to the database
	client = MongoClient()
	db = client.turkishElection                              # choose a database
	collection = db.timelinewithheld                             # choose a collection
	findoriginal(collection)
