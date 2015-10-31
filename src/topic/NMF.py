# -*- coding: utf-8 -*-

# Created by Yun Zhou to generate preprocessed 
# tweets data for the lda learner program
from pymongo import MongoClient
from sets import Set
import datetime
import pickle
import nltk.data

# figure out how data.load works
tokenizer = nltk.data.load('tokenizers/punkt/turkish.pickle')
stopwords = ['``', ';', "'", '+' ,'(',')',"''", ':','http','#','@','.','..','...',',','?','!','-','https','...','a','acaba', 'altm\xc4\xb1\xc5\x9f', 'alt\xc4\xb1', 'ama', 'ancak', 'arada', 'asl\xc4\xb1nda', 'ayr\xc4\xb1ca', 'bana', 'baz\xc4\xb1', 'belki', 'ben', 'benden', 'beni', 'benim', 'beri', 'be\xc5\x9f', 'bile', 'bin', 'bir', 'bir\xc3\xa7ok', 'biri', 'birka\xc3\xa7', 'birkez', 'bir\xc5\x9fey', 'bir\xc5\x9feyi', 'biz', 'bize', 'bizden', 'bizi', 'bizim', 'b\xc3\xb6yle', 'b\xc3\xb6ylece', 'bu', 'buna', 'bunda', 'bundan', 'bunlar', 'bunlar\xc4\xb1', 'bunlar\xc4\xb1n', 'bunu', 'bunun', 'burada', '\xc3\xa7ok', '\xc3\xa7\xc3\xbcnk\xc3\xbc', 'da', 'daha', 'dahi', 'de', 'defa', 'de\xc4\x9fil', 'di\xc4\x9fer', 'diye', 'doksan', 'dokuz', 'dolay\xc4\xb1', 'dolay\xc4\xb1s\xc4\xb1yla', 'd\xc3\xb6rt', 'edecek', 'eden', 'ederek', 'edilecek', 'ediliyor', 'edilmesi', 'ediyor', 'e\xc4\x9fer', 'elli', 'en', 'etmesi', 'etti', 'etti\xc4\x9fi', 'etti\xc4\x9fini', 'gibi', 'g\xc3\xb6re', 'halen', 'hangi', 'hatta', 'hem', 'hen\xc3\xbcz', 'hep', 'hepsi', 'her', 'herhangi', 'herkesin', 'hi\xc3\xa7', 'hi\xc3\xa7bir', 'i\xc3\xa7in', 'iki', 'ile', 'ilgili', 'ise', 'i\xc5\x9fte', 'itibaren', 'itibariyle', 'kadar', 'kar\xc5\x9f\xc4\xb1n', 'katrilyon', 'kendi', 'kendilerine', 'kendini', 'kendisi', 'kendisine', 'kendisini', 'kez', 'ki', 'kim', 'kimden', 'kime', 'kimi', 'kimse', 'k\xc4\xb1rk', 'milyar', 'milyon', 'mu', 'm\xc3\xbc', 'm\xc4\xb1', 'nas\xc4\xb1l', 'ne', 'neden', 'nedenle', 'nerde', 'nerede', 'nereye', 'niye', 'ni\xc3\xa7in', 'o', 'olan', 'olarak', 'oldu', 'oldu\xc4\x9fu', 'oldu\xc4\x9funu', 'olduklar\xc4\xb1n\xc4\xb1', 'olmad\xc4\xb1', 'olmad\xc4\xb1\xc4\x9f\xc4\xb1', 'olmak', 'olmas\xc4\xb1', 'olmayan', 'olmaz', 'olsa', 'olsun', 'olup', 'olur', 'olursa', 'oluyor', 'on', 'ona', 'ondan', 'onlar', 'onlardan', 'onlar\xc4\xb1', 'onlar\xc4\xb1n', 'onu', 'onun', 'otuz', 'oysa', '\xc3\xb6yle', 'pek', 'ra\xc4\x9fmen', 'sadece', 'sanki', 'sekiz', 'seksen', 'sen', 'senden', 'seni', 'senin', 'siz', 'sizden', 'sizi', 'sizin', '\xc5\x9fey', '\xc5\x9feyden', '\xc5\x9feyi', '\xc5\x9feyler', '\xc5\x9f\xc3\xb6yle', '\xc5\x9fu', '\xc5\x9funa', '\xc5\x9funda', '\xc5\x9fundan', '\xc5\x9funlar\xc4\xb1', '\xc5\x9funu', 'taraf\xc4\xb1ndan', 'trilyon', 't\xc3\xbcm', '\xc3\xbc\xc3\xa7', '\xc3\xbczere', 'var', 'vard\xc4\xb1', 've', 'veya', 'ya', 'yani', 'yapacak', 'yap\xc4\xb1lan', 'yap\xc4\xb1lmas\xc4\xb1', 'yap\xc4\xb1yor', 'yapmak', 'yapt\xc4\xb1', 'yapt\xc4\xb1\xc4\x9f\xc4\xb1', 'yapt\xc4\xb1\xc4\x9f\xc4\xb1n\xc4\xb1', 'yapt\xc4\xb1klar\xc4\xb1', 'yedi', 'yerine', 'yetmi\xc5\x9f', 'yine', 'yirmi', 'yoksa', 'y\xc3\xbcz', 'zaten']
# withheld = [1512118374, 1528527474, 2775606467, 2776783461, 323353537, 111437703, 2872713657, 2961800735, 516578419, 2567892499, 201035925, 2999695853, 1927671576, 2777554767, 2938117259, 2204006713, 835529077, 144910421, 2436878456, 536664198, 2811033792, 2230165195, 1587735252, 2765416702, 2354700919, 210913570, 1668569444, 2696366440, 2180309453, 2560901623, 2257902144, 2827063876, 1860629066, 2306253432, 1604469463, 1074928730, 2340758401, 2597972893, 738855900, 2282587194, 240055365, 536366335, 2317733082, 897072415, 566441316, 1084267908, 64050823]
withheld = [1512118374, 1528527474, 2775606467, 2776783461, 323353537, 111437703, 2872713657, 2961800735, 516578419, 2567892499, 201035925, 2999695853, 1927671576, 2777554767, 2938117259, 2204006713, 835529077, 144910421, 2436878456, 536664198, 2811033792, 2230165195, 1587735252, 2765416702, 2354700919, 210913570, 1668569444, 2696366440, 2180309453, 2560901623, 2257902144, 2827063876, 1860629066, 2306253432, 1604469463, 1074928730, 2340758401, 2597972893, 738855900, 2282587194, 240055365, 536366335, 2317733082, 897072415, 566441316, 1084267908, 64050823]


class Tweet:
    def __init__(self, tweet_id, text, hashtags, created_at, domains):
        self.tweet_id = tweet_id
        self.text = text
        self.hashtags = hashtags
        self.created_at = created_at
        self.domains = domains

    def __str__(self):
        return "Content: %s \nCreated: %s" % (self.get_content(), self.created_at)


# low = datetime.datetime.strptime("2014-10-05", "%Y-%m-%d")
# high = datetime.datetime.strptime("2014-10-25", "%Y-%m-%d")


def checktime(tweet):
    time = tweet[u'created_at']
    dt = datetime.datetime.strptime(time, '%a %b %d %H:%M:%S +0000 %Y')  # format the time
    start_time = datetime.datetime(2015, 6, 23)   
    end_time = datetime.datetime(2015, 6, 26)   
    if start_time <= dt <= end_time:   
        return True
    return False


def runmain():    
    tweetes = []
    duplicate = Set([])
    counter = 0
    for tweet in collection.find():

        # if tweet[u'user'][u'id'] not in withheld:
            text = tweet[u'text']
            # if (text in duplicate):
            #    continue
            # else:
            #    duplicate.add(text)
            if checktime(tweet):
                tweetes.append(tokenizer.tokenize(text)[0].encode("utf-8"))
            counter += 1  
            if counter % 1000 == 0:
                print "Found %s tweets" % counter

    print "Start feature extraction"

    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.decomposition import NMF

    dataset = tweetes

    n_features = 500
    n_topics = 2
    n_top_words = 10

    vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=n_features,
                                 stop_words=stopwords)
    print type(dataset)
    print len(dataset)
    
    tfidf = vectorizer.fit_transform(dataset)
    print "Fitting the NMF model with n_samples=%d and n_features=%d..." % (len(dataset), n_features)
    nmf = NMF(n_components=n_topics, random_state=1).fit(tfidf)

    feature_names = vectorizer.get_feature_names()

    for topic_idx, topic in enumerate(nmf.components_):
        print "Topic #%d:" % topic_idx
        print " ".join([feature_names[i].encode("utf-8") for i in topic.argsort()[:-n_top_words - 1:-1]])
        print


if __name__ == '__main__':
    # Connect to the database
    client = MongoClient()
    db = client.turkishElection                              # choose a database
    collection = db.postwithheld                             # choose a collection

    print "this is main"
    runmain()
    count = 0
    # for tweet in collection.find():
    #     #print tweet[u'withheld_in_countries'][0] == "BR"
    #     if "TR" in tweet[u'withheld_in_countries'][0] == "TR":
    #         count += 1
    # print count
    # for i in withheld:
    #     if i not in new:
    #         new.append(i)
    # print new
    # print len(new)

# Topic #0:
# diyarbakır rt hdp nin mitingine oy mitinginde işid yilmazgedik bombalı
# name of the city; rt; hdp; nin; rally; Islamic State of Iraq and the Levant; YilmazGedik is an account name; bomb

# Topic #1:
# türkiye akp chp mhp geneli 25 açılan sandık 12 16

# Topic #2:
# co lan mühürlü kulp bulundu nde lisesi yırtılmış sandığınasahipcık oylar
# related election fraud talking about damaged vote box

# Topic #3:
# demirtasdiyarbakırda amed jı gün yarın halkın amede doğacak umudu başka
# related to Diyarbakir kurd bombing

# Topic #4:
# su_sahinn bi geliyor hiç değil li öyle yok sorun tabi



