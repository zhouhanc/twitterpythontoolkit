# -*- coding: utf-8 -*-
"""
	@
	@Description:   This script compare two list of users from two files
    @               
    @Author:        Joe Chen
    @Last modified: 10/25/2015 
"""
import pprint
def compare(fa, fb):
	user1 = []
	with open(fa, "r") as f:
		for line in f:
			user1.append(int(line))
	user2 = []
	with open(fb, "r") as f:
		for line in f:
			user2.append(int(line))			
	# frifollo = set([2257902144, 3401486913, 3431181573, 2288471878, 3399748936, 3722380589, 3395597584, 1374335251, 2575621397, 3315164850, 2948800306, 1531270172, 3570004037, 2511233055, 3418161376, 3645368482, 2403119414, 2693834406, 3121649989, 388287016, 3253090793, 845909546, 2800030829, 3803601797, 3012885232, 3331194418, 2801065461, 934557302, 761966095, 3889700794, 3376421500, 418664573, 3422414015])
	print len(user1)
	print len(user2)
	print "number of common users are"
	
	print set(user1).intersection(set(user2))
	print len(set(user1).intersection(set(user2)))

	# print "test if friend follow withheld are all in our new database"
	# print len(frifollo)
	# print len(set(user1).intersection(frifollo))

	# print "test if friend follow withheld are not in our old withheld user"
	# print len(set(user2).intersection(frifollo))

if __name__ == '__main__':
	import sys
	compare(sys.argv[1], sys.argv[2])




	