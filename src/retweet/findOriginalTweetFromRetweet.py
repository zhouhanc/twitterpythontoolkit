# -*- coding: utf-8 -*-
"""
	@
    @Description:   This script finds the original tweet of a retweet
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
from collections import defaultdict

def findOriginal(filename):

	count = 0
	dicText = defaultdict(int)
	with open(filename) as f:

		for line in f:
			tweet = json.loads(line)
			text = tweet[u'text']

			if u"RT @AJALive: عاجل | مراسل #الجزيرة: الحوثيون يحركون لواء مدفعية من #صعدة إلى الملاحيط الحدودية مع #السعودية" in text:
				print tweet[u"source"]
				dicText[tweet[u"source"]] += 1
				pprint.pprint(tweet, width=1) 
				exit(0)

			count += 1

			if count % 5000 == 0:
				print count

			
	print "length of the dic is --> ", len(dicText)
	print dicText




if __name__ == '__main__':

	client = MongoClient()                       # connect to the server             
	db = client.yemen             				 # choose a database   
	collection = db.posts              		     # choose a collection 


	findOriginal("../usual.json")








