# -*- coding: utf-8 -*-
"""
	@
    @Description:   This script finds top k source
    @               
    @               
    @Author:        Joe Chen
    @Last modified: 10/10/2015 

"""
import time
import ujson as json
import pymongo
from pymongo import MongoClient
from collections import defaultdict


def findSource(collection, numprint = 20):
	"""prints a dictionary of sources"""
	count = 0
	dic = defaultdict(int)
	for tweet in collection.find():
			
			dic[tweet[u'source']] += 1
			count += 1

			if count % 5000 == 0:
				print count
			
	print "number of distinct source is --->", len(dic) 

	import operator 
	dic_sorted = sorted(dic.items(), key=operator.itemgetter(1), reverse = True)
	
	for x in dic_sorted[:int(numprint)]:
		print x[0].encode("utf-8", "ignore"), ",", x[1]

	



if __name__ == '__main__':

	start = time.time()

	client = MongoClient()                	 	# connect to the server             
	db = client.turkishElection             				 # choose a database   
	collection = db.postwithheld              				 # choose a collection 

	findSource()

	end = time.time()