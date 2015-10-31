# -*- coding: utf-8 -*-
"""
	@
    @Description:   This script goes over all tweets created by one user
    @               
    @               
    @Author:        Joe Chen
    @Last modified: 09/19/2015
"""
import time
import json
import pymongo
from pymongo import MongoClient
from collections import defaultdict
import pickle
import pprint 


def checkSource(data, userid):
	"""check the source of a group of tweets"""
	# Open a file for writing
	
	total = 0
 	src = defaultdict(int)

	for tweet in data:

		if tweet[u'user'][u'id_str'] == userid:
			total += 1
			if (total % 5000 == 0):
				print ("read " + str(total) + " tweets now" )

			src[tweet[u'source']] += 1
			
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(src)
	

def checkText(userid):
	""" check the text of a group of tweets"""
	
	total = 0
 	src = defaultdict(int)

	for tweet in data:

		if tweet[u'user'][u'id_str'] == userid:
			total += 1
			if (total % 1000 == 0):
				print tweet[u'text'].encode("utf-8", "ignore")
				print ("read " + str(total) + " tweets now" )


def checkHashtag(data):
	""" check the hashtag of a group of tweets"""
	dic = defaultdict(int)

	for tweet in data:
			text = tweet[u'text']
			occ = text.count('#')
			dic[occ] += 1	

	print dic



def loadFromFile(filename):

	print "start loading json..."
	with open(filename) as json_file:
		json_data = json.load(json_file)
	print "finish loading json!!!"
	return json_data

if __name__ == '__main__':

	start = time.time()

	client = MongoClient()                	 				 # connect to the server             
	db = client.turkishElection             				 # choose a database   
	collection = db.postwithheld              				 # choose a collection 

	
	data = loadFromFile("top10UsersTweet.json")
	#checkSource(data)
	#checkText(data)
	checkHashtag(data)

	end = time.time()

