# -*- coding: utf-8 -*-
"""
	@
    @Description:   This script finds top k frequent words
    @               
    @               
    @Author:        Joe Chen
    @Last modified: 09/18/2015 

"""
import time
import ujson as json
import pymongo
from pymongo import MongoClient
from collections import defaultdict


def frequentUser(collection, nprint=100, store = 0, outputfilename = "../output/frequentuser.txt"):
	"""prints a dictionary of users that generated the most number of tweets"""

	count = 0
	dic = defaultdict(int)
	for tweet in collection.find():

			_id = tweet[u'user'][u'id_str']
			dic[_id] += 1
			count += 1

			if count % 5000 == 0:
				print count
			
	print "number of distinct users is -->", len(dic) 
	print "Here is the list of users"
	print dic.keys()

	if int(store) == -1:
		print "write a list of users into a file"		
		f = open("ALLUSER_" + str(len(dic)) + ".txt", 'w')
		for user in set(dic.keys()):
			f.write(str(user) + "\n")
		f.close()

	print "TOP " + str(nprint) + " users========================"

	import operator 
	dic_sorted = sorted(dic.items(), key=operator.itemgetter(1), reverse = True)
	for x in dic_sorted[1:int(nprint)]:
		print x

	# write the result to a file
	if store > 0:
		f = open(outputfilename, 'w')

		print "STORE TOP ", str(store), " users into a file ========================"

		for i in dic_sorted[:int(store)]:
			f.write(str(i) + '\n')

		f.close()
		print "Finish writing to a file"

if __name__ == '__main__':

	start = time.time()

	client = MongoClient()                	 	# connect to the server             
	db = client.turkishElection             				 # choose a database   
	collection = db.postwithheld              				 # choose a collection 

	frequentUser()

	end = time.time()

