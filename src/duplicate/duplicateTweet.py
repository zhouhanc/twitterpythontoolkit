# -*- coding: utf-8 -*-
"""
	@
    @Description:   This script checks duplicate tweets
    @               
    @               
    @               
    @Author:        Joe Chen
    @Last modified: 09/12/2015
"""
import pprint
import time
import ujson as json
import os
import pymongo
import datetime 
import itertools
from pymongo import MongoClient

def duplicate(collection, nprint = 20, store = 0, outputfilename = "../output/duplicate.txt"):

	count = 0
	dicText = {}
	for tweet in collection.find():

		# check if the tweet is duplicate or not
		#if u'retweeted_status' in tweet:

			text = tweet[u'text']
			if dicText.has_key(text):
				dicText[text]["count"]+=1
				dicText[text]["ids"].append(tweet[u'user'][u'id_str'])
			else:
				dicText[text]={"count":1, "ids":[tweet[u'user'][u'id_str']]}
			
			count += 1

			if count % 5000 == 0:
				print count
			
	print "number of duplicate tweet is --> ", len(dicText)
	import operator

	sorted_dicText = sorted(dicText.items(), key=operator.itemgetter(1), reverse = True)

	print "TOP " + str(nprint) + " duplicates========================"
	count = 1
	for i in sorted_dicText[:int(nprint)]:
		print "TOP " + str(count)
		count += 1
		print "number of occurrences --> ", i[1]["count"]
		#print i[1]["ids"]
		print i[0].encode("utf-8", "ignore")
		print "-----------------------------"
		print 

	# write the result to a file
	if store > 0:

		f = open(outputfilename, 'w')

		print "STORE TOP ", str(store), " tweets into a file ========================"

		for i in sorted_dicText[:int(store)]:
			f.write('>' + str(i[1]["count"]) + '\n')
			f.write(str(i[0].encode("utf-8", "ignore")) + '\n')
			f.write(str(i[1]["ids"]) + '\n')

		f.close()
		print "Finish writing to a file"


if __name__ == '__main__':

	duplicate()






