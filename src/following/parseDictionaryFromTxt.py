import datetime 
import pprint
from collections import defaultdict
import re
import pickle
from sets import Set

# parse user and its follower

user_dic = {}

def parseUser(filename):
	
	f = open(filename + ".txt", 'r')

	for line in f:
		
		follower_list = line.split(',')
		# parse the user
		user = follower_list[0][:-1]
		if follower_list[-1][-1] == "\n":
			follower_list[-1] = follower_list[-1][:-1]
		
		# delete the first entry, which is the user
		del follower_list[0]
		
		# store key, value pair into dictionary
		user_dic[user] = follower_list

		print "finish one user"

	f.close()

	""">>>>>>>>>>> 
				   At this point, user_dic has stored all information, 
				   one can commend out the following section of code if 
				   necessary.
	   <<<<<<<<<<<<"""


	####################################################################
	# make sure all followers are also a key in the user_dic dictionary
	# print "start updating the dictionary-------->"
	# key_set = Set(user_dic.keys())
	# for key in user_dic.keys():
		
	# 	# change it to set operation; set intersection
	# 	new_val = key_set.intersection(Set(user_dic[key]))
	# 	#new_val = [val for val in user_fol[key] if val in user_fol.keys()]
	# 	user_dic[key] = list(new_val)

	# print "finish updating, return dictionary now --------->"
	####################################################################

	# print "length before cleaning up ", len(user_dic)
	# print len([key for key in user_dic.keys() if len(user_dic[key]) < 4] )

	# # 4: 4136
	# # 3: 4021
	# # 2: 3809

	# infrequent_users = Set( [key for key in user_dic.keys() if len(user_dic[key]) < 4]  )

	# for key in user_dic.keys():
	# 	new_value = infrequent_users.intersection(Set(user_dic[key]))
	# 	user_dic[key] = new_value

	# for user in infrequent_users:
	# 	user_dic.pop(user, None)
	# 	#del user_dic[user]

	# print "length after cleaning up ", len(user_dic)

	# store the dictionary into a pickle file for later use
	print "start pumping dic to pickle"
	print "length of dic is --> ", len(user_dic)
	s = 0
	for key in user_dic.keys():
		s += len(user_dic[key])
		print key, len(user_dic[key])
	print s

	pickle.dump( user_dic, open( filename + ".p", "wb" ) )

	print "finish pumping dic to pickle"


if __name__ == '__main__':

	# This program will read a dictionry from a txt file and 
	# write the result to a pickle file for later user. The 
	# dictionary can also be used directly

	"""======== Change the filename ========"""
	filename = "allFollowers"
	parseUser(filename)




