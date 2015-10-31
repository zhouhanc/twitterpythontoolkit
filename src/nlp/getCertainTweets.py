# -*- coding: utf-8 -*-
"""
	@
	@Description:   This script finds and stores tweets based on certain creteria
    @               
    @Author:        Joe Chen
    @Last modified: 10/28/2015 

"""
import time
import json
from pymongo import MongoClient
import datetime
import imp


def NoOp(arg):
	return True

def getter(collection, modulename=None, filename="AlltweetsNoOp.json"):
    """get and store tweets based on a given function"""
    count = 0
    print "total number of tweets in this database is ", collection.find().count()
    # open a new file   ###
    outfile = open(filename, "w")
    # according to the json list format 
    outfile.write("[")
    if modulename == None:
    	option = NoOp
    else:
    	module = imp.load_source('module.name', modulename)
        option = module.check

	for tweet in collection.find():
			count += 1
			if count % 5000 == 0:
				print count
			if option(tweet):
				tweet.pop(u'_id', None)
				json.dump(tweet, outfile, indent = 4)
				outfile.write(",")

    # close all files
    outfile.seek(-1, 1)
    outfile.write("]")
    outfile.close() 
    print "finish writing to the file"

if __name__ == '__main__':
	client = MongoClient()
	db = client.turkishElection
	collection = db.postwithheld
	getter(collection, "/Users/zc/Documents/twitter_research/twitterpythontoolkit/src/nlp/checkword.py")
