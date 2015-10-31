# -*- coding: utf-8 -*-
"""
	@
    @Description:   This script finds top k frequent words
    @               
    @               
    @Author:        Joe Chen
    @Last modified: 07/09/2015 

"""
import time
import ujson as json
import pymongo
from pymongo import MongoClient
import nltk
from nltk.stem.snowball import SnowballStemmer
import datetime


stopwords = [ "|", "&" , "[", "]",  "'",';',"'s",'-','``','(',')',"''", ':','http','#','@','.','..','...',',','?','!','https','...','a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by','can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my','neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so','some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what','when','where','which','while','who','whom','why','will','with','would','yet','you','your']
stemmer = SnowballStemmer("english")



def NoOp(arg):
	return True


def checkTime(tweet):
	time = tweet[u'created_at']
	dt = datetime.datetime.strptime(time, '%a %b %d %H:%M:%S +0000 %Y')  # format the time
	start_time = datetime.datetime(2015, 6, 6)   
	end_time = datetime.datetime(2015, 6, 10)   
	if  start_time <= dt <= end_time:	
		return True
	return False

def Tokenizer(collection, option = NoOp):
	count = 0
	tokenized_tweet = []
	print "total number of tweets in this database is ", collection.find().count()
	
	
	for tweet in collection.find():

			
			count += 1
			if count % 5000 == 0:
				print count

			if option(tweet):
				tokens = nltk.word_tokenize(tweet[u'text'].lower())
				for token in tokens:
					if token not in stopwords:
						tokenized_tweet.append(stemmer.stem(token))

	return tokenized_tweet




def get_frequency(tokens, numofwords):
	"""
	Output: a list of numofwords elements
	"""
	print "get distribution"
	fdist1 = nltk.FreqDist(tokens)
	return fdist1.most_common(numofwords)

def getTopk(text, topk):
	"""print out the top k frequent words"""
	freq = get_frequency(text, topk)
	
	for x in xrange(0,topk):
		if str(freq[x][0].encode("utf-8")) not in stopwords:
			print str(x) + "-->" + str(freq[x][0].encode("utf-8"))
			#print str(x) + "     " + str(region_token[x][0].encode("utf-8"))

def frequentwords(collection, num = 20):
	getTopk(Tokenizer(collection), int(num))



if __name__ == '__main__':

	"""	
		Input: db name, collection name, num: top number of words
		Output: print top num of words

	"""

	client = MongoClient()                	 	# connect to the server             
	db = client.turkishElection             				 # choose a database   
	collection = db.postwithheld              				 # choose a collection 

	num  = 200

	#userstat()

	#Tokenizer(collection)
	getTopk(Tokenizer(collection), num)





