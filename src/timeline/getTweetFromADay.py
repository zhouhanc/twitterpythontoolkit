# -*- coding: utf-8 -*-
"""
	@
    @Description:   This script prints tweets on a given day
    @               
    @               
    @Author:        Joe Chen
    @Last modified: 30/09/2015 

"""
import time
import ujson as json
import pymongo
from pymongo import MongoClient
from collections import defaultdict
import datetime


def findSource():
	"""prints a dictionary of users that generated the most number of tweets"""
	count = 0
	dic = defaultdict(int)
	for tweet in collection.find():

		time = tweet[u'created_at']
		dt = datetime.datetime.strptime(time, '%a %b %d %H:%M:%S +0000 %Y')  # format the time
		start_time = datetime.datetime(2015, 6, 25)   
		end_time = datetime.datetime(2015, 6, 26)   
		if  start_time <= dt <= end_time:

			dic[tweet[u'source']] += 1
			count += 1

			if count % 5000 == 0:
				print count
			
	print "length of dic", len(dic) 





if __name__ == '__main__':

	start = time.time()

	client = MongoClient()                	 	# connect to the server             
	db = client.turkishElection             				 # choose a database   
	collection = db.postwithheld              				 # choose a collection 

	findSource()

	end = time.time()