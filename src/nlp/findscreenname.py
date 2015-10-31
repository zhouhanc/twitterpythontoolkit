# -*- coding: utf-8 -*-
"""
	@
	@Description:   This script finds the screen name and return a list of screennames corresponding to 
	@				
    @               
    @Author:        Joe Chen
    @Last modified: 10/28/2015 

"""
import time
import json
from pymongo import MongoClient
import datetime
import pickle
import sys


def findsn(collection, filename, outfile):
	"""
	Find screennames for a list of users
	Input:  a pickle file
	Output: a list of strings
	"""
	user_fol = pickle.load(open(filename, "rb"))
	user_fol.keys()
	new_dic = {}
	count = 0
	for key in user_fol.keys():
		
		new_dic[key] = None
		

	# note: not all users exist
	print len(new_dic)
	for tweet in collection.find():
		count += 1
		if count % 5000 == 0:
			print count
		
		if tweet[u'user'][u'id_str'] in new_dic:
			new_dic[tweet[u'user'][u'id_str']] = tweet[u'user'][u'screen_name']

	# store a list of screennames
	pickle.dump(new_dic, open(outfile + ".p", "wb"))
	print new_dic.values()
	# return new_dic.values()

if __name__ == '__main__':

	client = MongoClient()
	db = client.TE
	collection = db.election
	findsn(collection, sys.argv[1], sys.argv[2])



