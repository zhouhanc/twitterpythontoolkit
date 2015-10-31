
import cmd
from pymongo import MongoClient

from duplicate import duplicateTweet
from timeline import timeline
from retweet import findRetweet
from retweet import findOriginalUserFromRetweet
from retweet import findOriginalTweetFromRetweet
from user import frequentUsers
from user import getTweetFromUser
from source import source
from nlp import frequentWords
from nlp import topicClassifier
from nlp import getCertainTweets
from util import filecompare


class TwitterPython(cmd.Cmd):
    """Simple command processor example."""

    def store_collection(self, collec):
        """store the collection that will be shared by all methods"""
        self.collection = collec

    def do_duplicate(self, args):
        """duplicate [numprint] [numstore] [filename]
        find duplicate tweets 
        numprint (optinal, default = 20): number of top duplicate tweets to be printed
        numstore (optional, default = 0): number of top duplicate tweets to be stored
        filename (optional, default = ../output/duplicate.txt): the absolute path to the outout file
        example usage: duplicate 20, 100, /Users/zc/Documents/research/filename.txt"""

        args = args.split()
        if len(args) == 0:
            duplicateTweet.duplicate(self.collection)        
        elif len(args) == 1:
            duplicateTweet.duplicate(self.collection, args[0])
        elif len(args) == 2:
            duplicateTweet.duplicate(self.collection, args[0], args[1])            
        elif len(args) == 3:
            duplicateTweet.duplicate(self.collection, args[0], args[1], args[2])
        
    def do_frequentuser(self, args):
        """frequent user [numprint] [numstore] [filename]
        find users that tweet frequently (top k users), the program also prints a list of all distinct users  
        numprint (optinal, default = 100): number of top users to be printed
        numstore (optional, default = 0): number of top users to be stored, if numstore = -1, all usernames will be stored
        filename (optional, default = ../output/frequentuser.txt): the absolute path to the outout file
        example usage: frequent 20, 100, /Users/zc/Documents/research/filename.txt
        """

        args = args.split()
        if len(args) == 0:
            frequentUsers.frequentUser(self.collection)        
        elif len(args) == 1:
            frequentUsers.frequentUser(self.collection, args[0])
        elif len(args) == 2:
            frequentUsers.frequentUser(self.collection, args[0], args[1])            
        elif len(args) == 3:
            frequentUsers.frequentUser(self.collection, args[0], args[1], args[2])
        
    def do_plottimeline(self, args):
        """plottimeline [filename]
        plot the tweet distribution by day
        filename (optional, default = ../output/timeline.pdf): the absolute path to the outout file
        example usage: plottimeline /Users/zc/Documents/research/plot.pdf
        """

        args = args.split()
        if len(args) == 0:
            timeline.makeplot(self.collection, "../output/timeline.pdf")
        elif len(args) == 1:
            timeline.makeplot(self.collection, args[0])

    def do_countretweet(self, args):
        """countretweet 
        count the number of retweets
        
        example usage: countretweet 
        """

        findRetweet.findretweet(self.collection)

    def do_getOriginalUserFromRetweet(self, outputfile):
        """getOriginalUserFromRetweets [outputfile]
        get all original users from all retweets in current database
        outputfile (optional, default = ../output/OriginalUserFromRetweets.txt): the absolute path to the outout file
        example usage: getOriginalUserFromRetweets /Users/zc/Documents/research/original.txt 
        """

        if outputfile:
            findOriginalUserFromRetweet.findoriginal(self.collection, outputfile)
        else:
            findOriginalUserFromRetweet.findoriginal(self.collection)

    def do_checksource(self, args):
        """checksource [numprint]
        return a sorted dictionary of sources based on frequency
        numprint (optinal, default = 20): number of top sources to be printed
        example usage: checksource 10 
        """

        args = args.split()
        if len(args) == 0:
            source.findSource(self.collection)
        elif len(args) == 1:            
            source.findSource(self.collection, args[0])            

    def do_frequentword(self, num):
        """frequentword [num]
        return a sorted dictionary of words based on frequency
        num (optinal, default = 20): number of top words to be printed
        example usage: frequentword 100
        """

        if num:
            frequentWords.frequentwords(self.collection, num)
        else:      
            frequentWords.frequentwords(self.collection)

    def do_getAlltweetFromSomeUser(self, args):
        """getAlltweetFromOneUser [printout, outputfile]
           collects all retweets from a list of users in current database
           printout (optional, default = True): either True or False, which tells the program to print every single tweet or not
           outputfile (optional, default = None (no default value)): the absolute path to the outout file
           example usage: getAlltweetFromOneUser True /Users/zc/Documents/research/userA.json
        """

        username = raw_input('enter user name(s) (seperated by space):')
        username = username.split()
        args = args.split()
        if len(args) == 0:
            getTweetFromUser.gettweet(self.collection, username, "True")        
        elif len(args) == 1:
            getTweetFromUser.gettweet(self.collection, username, args[0])
        elif len(args) == 2:
            getTweetFromUser.gettweet(self.collection, username, args[0], args[1])            

    def do_filecompare(self, args):
        """filecompare [file1, file2]
           compare list of two users from two files
           file1: the absolute path to source file1
           file2: the absolute path to source file2
           example usage: filecompare a.txt b.txt
        """

        args = args.split()
        if len(args) != 2:
            print "invalid number of arguments, try again"
        else:
            filecompare.compare(args[0], args[1])

    def do_topicClassification(self, args):
        """topicClassification n_topic n_top_words
           Build tf-idf matrix and apply NMF to do topic classification
           n_topic (optinal, default = 5): number of topics 
           n_top_words (optinal, default = 20): number of words in each topic
           example usage: topicClassification 10 10
        """

        args = args.split()
        if len(args) == 0:
            topicClassifier.RunMain(self.collection)
        elif len(args) == 2:
            topicClassifier.RunMain(self.collection, args[0], args[1])
        else:
            print "invalid number of arguments, try again"

    def do_getcertainTweet(self, args):
        """do_getcertainTweet modulename filename
           find tweets based on a check() function and store those tweets into a json file
           modulename (required, default = None): the python script that contains a check function 
           filename (required, default = AlltweetsNoOp.json): filename of the output json file
           example usage: do_getcertainTweet checkword.py wordwithAKP.json
        """
        
        args = args.split()
        if len(args) == 2:
            getCertainTweets.getter(self.collection, args[0], args[1])
        else:
            print "invalid number of arguments, try again"

    def do_EOF(self, line):
        return True


def run():
    print "==========================================================="
    print 
    print "Welcome to TwitterPythonToolKit"
    print "Author: Joe (Zhouhan) Chen"
    print " _____          _ _   _            ____        _   _                 "
    print "|_   _|_      _(_) |_| |_ ___ _ __|  _ \ _   _| |_| |__   ___  _ __  "
    print "  | | \ \ /\ / / | __| __/ _ \ '__| |_) | | | | __| '_ \ / _ \| '_ \ "
    print "  | |  \ V  V /| | |_| ||  __/ |  |  __/| |_| | |_| | | | (_) | | | |"
    print "  |_|   \_/\_/ |_|\__|\__\___|_|  |_|    \__, |\__|_| |_|\___/|_| |_|"
    print "                                         |___/                       "

    print 
    print "Please enter database and collection \nname first to start connection"
    print "==========================================================="
    db_input = raw_input('enter database name:')
    collection_input = raw_input('enter collection name:')

    # db_input = "turkishElection"
    # collection_input = "postwithheld"

    client = MongoClient()
    db = client[db_input]
    collection = db[collection_input]

    if collection.count() == 0:
        print "WARNING: the collection you chose has 0 entry, \nplease check the name again"
    else:
        print "==========================================================="
        print "This collection has " + str(collection.count()) + " entries"
    TP = TwitterPython()
    TP.store_collection(collection)
    TP.cmdloop()


if __name__ == '__main__':
    run()






