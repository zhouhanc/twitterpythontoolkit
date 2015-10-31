# -*- coding: utf-8 -*-
"""
	@
    @Description:   This script counts number of retweets
    @               
    @               
    @               
    @Author:        Joe Chen
    @Last modified: 09/30/2015
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

def findretweet(collection):

	count = 0
	retweet = 0
	dicText = defaultdict(int)
	for tweet in collection.find():

		if u'retweeted_status' in tweet:
			retweet += 1

		count += 1
		if count % 5000 == 0:
			print count

			
	print "num of retweet is --> ", retweet





if __name__ == '__main__':

	client = MongoClient()                	 				 # connect to the server             
	db = client.turkishElection             				 # choose a database   
	collection = db.postwithheld              				 # choose a collection 

	findretweet()

