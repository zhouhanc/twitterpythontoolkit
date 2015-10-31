# -*- coding: utf-8 -*-
"""
	@
    @Description:   This script gets all tweets from a list of user
    @               
    @               
    @Author:        Joe Chen
    @Last modified: 09/18/2015 
"""
import time
import json
import pymongo
from pymongo import MongoClient
from collections import defaultdict
import pickle

def tweetfromuser(collection, printout = True, filename = None):

	count = 0
	for tweet in collection.find():

			_id = tweet[u'user'][u'id_str']
			if _id in interest_user.keys():
				interest_user[_id].append(tweet)

				if printout:
					print _id
					print tweet[u'text'].encode("utf-8", "ignore")
					print tweet[u'created_at']
					print 

			count += 1
			if count % 5000 == 0:
				print count
	
	# print "length of interest_user", len(interest_user) 
	if filename != None:
		print "start writing to file"

		writeToFile(filename, interest_user)

		print "finish writing to file"
	

def writeToFile(filename, dic):
	# Open a file for writing
	out_file = open(filename,"w")
	total = 0
	output_list = []
 
	for key in dic.keys():
		for tweet in dic[key]:
			total += 1
			if (total % 5000 == 0):
				print ("read " + str(total) + " tweets now" )

			tweet.pop(u'_id', None)
			output_list.append(tweet)
			#json.dump(tweet , out_file, indent=4)
	# Close the file
	json.dump(output_list, out_file, indent=4)
	out_file.close()
	print("---number of selected tweets are " + str(total) + "-----")

def gettweet(collection, userlist, printout = 'True', filename = None):
	global interest_user
	interest_user = {}
	for item in userlist:
		interest_user[item] = []
	
	if printout == 'True':
		po = True
	elif printout == 'False':
		po = False
	else:
		print "found neither True nor False"
		raise ValueError
	tweetfromuser(collection, po, filename)


if __name__ == '__main__':
	start = time.time()

	client = MongoClient()                	 	# connect to the server             
	db = client.turkishElection             				 # choose a database   
	collection = db.postwithheld              				 # choose a collection 

	l = [u'1468619406']
	interest_user = {}
	for item in l:
		interest_user[item] = []
	print interest_user

	tweetfromuser(collection, True)
	end = time.time()

