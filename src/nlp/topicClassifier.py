# -*- coding: utf-8 -*-

# Created by Yun Zhou to generate preprocessed 
# tweets data for the lda learner program
from pymongo import MongoClient
from urlparse import urlparse
import datetime
import pickle
import nltk.data
import re
import ijson
import ujson as json

# figure out how data.load works
tokenizer = nltk.data.load('tokenizers/punkt/turkish.pickle')

stopwords = ['``', ';', "'", '+' ,'(',')',"''", ':','http','#','@','.','..','...',',','?','!','-','https','...','a','acaba', 'altm\xc4\xb1\xc5\x9f', 'alt\xc4\xb1', 'ama', 'ancak', 'arada', 'asl\xc4\xb1nda', 'ayr\xc4\xb1ca', 'bana', 'baz\xc4\xb1', 'belki', 'ben', 'benden', 'beni', 'benim', 'beri', 'be\xc5\x9f', 'bile', 'bin', 'bir', 'bir\xc3\xa7ok', 'biri', 'birka\xc3\xa7', 'birkez', 'bir\xc5\x9fey', 'bir\xc5\x9feyi', 'biz', 'bize', 'bizden', 'bizi', 'bizim', 'b\xc3\xb6yle', 'b\xc3\xb6ylece', 'bu', 'buna', 'bunda', 'bundan', 'bunlar', 'bunlar\xc4\xb1', 'bunlar\xc4\xb1n', 'bunu', 'bunun', 'burada', '\xc3\xa7ok', '\xc3\xa7\xc3\xbcnk\xc3\xbc', 'da', 'daha', 'dahi', 'de', 'defa', 'de\xc4\x9fil', 'di\xc4\x9fer', 'diye', 'doksan', 'dokuz', 'dolay\xc4\xb1', 'dolay\xc4\xb1s\xc4\xb1yla', 'd\xc3\xb6rt', 'edecek', 'eden', 'ederek', 'edilecek', 'ediliyor', 'edilmesi', 'ediyor', 'e\xc4\x9fer', 'elli', 'en', 'etmesi', 'etti', 'etti\xc4\x9fi', 'etti\xc4\x9fini', 'gibi', 'g\xc3\xb6re', 'halen', 'hangi', 'hatta', 'hem', 'hen\xc3\xbcz', 'hep', 'hepsi', 'her', 'herhangi', 'herkesin', 'hi\xc3\xa7', 'hi\xc3\xa7bir', 'i\xc3\xa7in', 'iki', 'ile', 'ilgili', 'ise', 'i\xc5\x9fte', 'itibaren', 'itibariyle', 'kadar', 'kar\xc5\x9f\xc4\xb1n', 'katrilyon', 'kendi', 'kendilerine', 'kendini', 'kendisi', 'kendisine', 'kendisini', 'kez', 'ki', 'kim', 'kimden', 'kime', 'kimi', 'kimse', 'k\xc4\xb1rk', 'milyar', 'milyon', 'mu', 'm\xc3\xbc', 'm\xc4\xb1', 'nas\xc4\xb1l', 'ne', 'neden', 'nedenle', 'nerde', 'nerede', 'nereye', 'niye', 'ni\xc3\xa7in', 'o', 'olan', 'olarak', 'oldu', 'oldu\xc4\x9fu', 'oldu\xc4\x9funu', 'olduklar\xc4\xb1n\xc4\xb1', 'olmad\xc4\xb1', 'olmad\xc4\xb1\xc4\x9f\xc4\xb1', 'olmak', 'olmas\xc4\xb1', 'olmayan', 'olmaz', 'olsa', 'olsun', 'olup', 'olur', 'olursa', 'oluyor', 'on', 'ona', 'ondan', 'onlar', 'onlardan', 'onlar\xc4\xb1', 'onlar\xc4\xb1n', 'onu', 'onun', 'otuz', 'oysa', '\xc3\xb6yle', 'pek', 'ra\xc4\x9fmen', 'sadece', 'sanki', 'sekiz', 'seksen', 'sen', 'senden', 'seni', 'senin', 'siz', 'sizden', 'sizi', 'sizin', '\xc5\x9fey', '\xc5\x9feyden', '\xc5\x9feyi', '\xc5\x9feyler', '\xc5\x9f\xc3\xb6yle', '\xc5\x9fu', '\xc5\x9funa', '\xc5\x9funda', '\xc5\x9fundan', '\xc5\x9funlar\xc4\xb1', '\xc5\x9funu', 'taraf\xc4\xb1ndan', 'trilyon', 't\xc3\xbcm', '\xc3\xbc\xc3\xa7', '\xc3\xbczere', 'var', 'vard\xc4\xb1', 've', 'veya', 'ya', 'yani', 'yapacak', 'yap\xc4\xb1lan', 'yap\xc4\xb1lmas\xc4\xb1', 'yap\xc4\xb1yor', 'yapmak', 'yapt\xc4\xb1', 'yapt\xc4\xb1\xc4\x9f\xc4\xb1', 'yapt\xc4\xb1\xc4\x9f\xc4\xb1n\xc4\xb1', 'yapt\xc4\xb1klar\xc4\xb1', 'yedi', 'yerine', 'yetmi\xc5\x9f', 'yine', 'yirmi', 'yoksa', 'y\xc3\xbcz', 'zaten']
# stopwords = [word.encode('utf-8') for word in stopwords_org]

# withheld = [1512118374, 1528527474, 2775606467, 2776783461, 323353537, 111437703, 2872713657, 2961800735, 516578419, 2567892499, 201035925, 2999695853, 1927671576, 2777554767, 2938117259, 2204006713, 835529077, 144910421, 2436878456, 536664198, 2811033792, 2230165195, 1587735252, 2765416702, 2354700919, 210913570, 1668569444, 2696366440, 2180309453, 2560901623, 2257902144, 2827063876, 1860629066, 2306253432, 1604469463, 1074928730, 2340758401, 2597972893, 738855900, 2282587194, 240055365, 536366335, 2317733082, 897072415, 566441316, 1084267908, 64050823]
# withheld = [1512118374, 1528527474, 2775606467, 2776783461, 323353537, 111437703, 2872713657, 2961800735, 516578419, 2567892499, 201035925, 2999695853, 1927671576, 2777554767, 2938117259, 2204006713, 835529077, 144910421, 2436878456, 536664198, 2811033792, 2230165195, 1587735252, 2765416702, 2354700919, 210913570, 1668569444, 2696366440, 2180309453, 2560901623, 2257902144, 2827063876, 1860629066, 2306253432, 1604469463, 1074928730, 2340758401, 2597972893, 738855900, 2282587194, 240055365, 536366335, 2317733082, 897072415, 566441316, 1084267908, 64050823]
# tokenizer = nltk.data.load('HK.pickle')

class Tweet:
    def __init__(self, tweet_id, text, hashtags, created_at, domains):
        self.tweet_id = tweet_id
        self.text = text
        self.hashtags = hashtags
        self.created_at = created_at
        self.domains = domains

    def get_content(self):
        result = self.text
        #append hashtags at the end of result
        if self.hashtags != None:
            result += ","
            for tag in self.hashtags:
                result += tag["text"]
                result += ","
        if self.domains != None:
            for domain in self.domains:
                result += domain
                result += ","
        return " ".join(tokenizer.tokenize(result))

    def __str__(self):
        return "Content: %s \nCreated: %s" % (self.get_content(), self.created_at)



#low = datetime.datetime.strptime("2014-10-05", "%Y-%m-%d")
#high = datetime.datetime.strptime("2014-10-25", "%Y-%m-%d")
withheld = set([2260094977, 2731534341, 1198835713, 427721047, 399308300, 761966095, 1561567248, 1112981522, 2971370008, 414128153, 2324177946, 2511233055, 1104046632, 486051369, 845909546, 3129314311, 2497534509, 763632175, 2850307120, 476129032, 2721640627, 2866130302, 2758156856, 2880136249, 3060195898, 2198510467, 3422949437, 3364479551, 2257902144, 435022913, 2932835906, 161037892, 3432704584, 1860629066, 895169611, 321283148, 388821075, 3320586836, 3432964695, 3149317209, 338459738, 2910107578, 1634200159, 2483631042, 487660641, 2225934435, 2282535014, 2427695208, 708070508, 854414354, 3390554301, 516578419, 418664573, 2604234517, 108722820, 83669126, 3020659335, 1582848648, 2700939031, 398196674, 1468619406, 3382954127, 463253648, 152621713, 2383857810, 3104648854, 3402723353, 383660696, 2893842586, 2956725915, 2821230753, 2464744725, 2693834406, 256969897, 2808943270, 3310244013, 804198577, 2834556083, 215943860, 3431544094, 85609142, 705236152, 405387961, 2459516192, 3388179645, 2812001471, 2965856032, 3296159942, 3431620815, 1455611089, 3421345493, 2678973661, 299287265, 1016020195, 2907405028, 1960960231, 2787092860, 2996805866, 3418805483, 2365751532, 3302784776, 388287016, 108902130, 1485058292, 3397389557, 2873735931, 2719756028, 2948934911, 3426694402, 3431181573, 2438241031, 321693960, 94900489, 594846987, 3312091571, 2982675731, 2575621397, 1327447831, 1927671576, 398998297, 2518761755, 3038611588, 268051742, 1149341984, 3217159971, 3394717989, 3414845225, 111437703, 2907606317, 2612009235, 2293151024, 3291829554, 3157860147, 2734487861, 2403119414, 2816108855, 2356447032, 605743417, 773522234, 3298522603, 428841793, 2938117259, 3419982664, 864677707, 2160688460, 3398538064, 1972824632, 3423770680, 2792222948, 223401306, 3397747552, 2269410145, 3332897123, 261414756, 1455117540, 3389645158, 607312231, 337634665, 1288647019, 2800030829, 3333352816, 3177141105, 551362418, 1963313012, 587547516, 3419559293, 841532286, 2797001602, 3398828147, 408618373, 3401486913, 222564497, 559363470, 3037836688, 499595164, 511546010, 1679318942, 2849218976, 2849619365, 3088416441, 3329327533, 366134685, 2882277809, 3173184947, 3454996456, 3346158010, 2405348796, 506546621, 383634366, 3371515840, 900525506, 2870950346, 2190516172, 1096976022, 553083855, 450227667, 193658840, 496123353, 2471859675, 3004110245, 2857575905, 1288644836, 55931558, 540353510, 2744836071, 2313947624, 1524713827, 2837399020, 3074858477, 968276462, 1632669680, 1534842866, 3402304499, 3397602293, 3296027126, 451604988])

def RunMain(collection, n_topics = 5, n_top_words = 20):    
    tweetes = []
    counter = 0
    for tweet in collection.find():
        #created_at = tweet[u'created_at']
        #dt = datetime.datetime.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y')
        #if low <= dt and dt <= high:
        #entries = tweet[u'entities']
        #urls = (e["url"] for e in entries["urls"])
        #expanded_urls = (e["expanded_url"] for e in entries["urls"])
        #domains = []
        # for url in expanded_urls:
        #     domain = get_domain(url.decode("ascii"))
        #     print "url: %s extracted domain: %s" % (url, domain)
        #     if domain:
        #         domains.append(uri.netloc)
        # print domains
        #tweet_id = str(tweet[u'id'])
        if int(tweet[u'user'][u'id']) not in withheld:
            text = tweet[u'text']
        #text = reduce(lambda t,s: t.replace(s, ""), urls, text)
        #hashtags = tweet[u'entities']['hashtags']
        #temp = Tweet(tweet_id, text, hashtags, created_at, domains)
        #print " ".join(tokenizer.tokenize(text))
        #print " ".join(tokenizer.tokenize(text)[0])
        #print len(tokenizer.tokenize(text))
        #print type(tokenizer.tokenize(text))
        #print tokenizer.tokenize(text)[0].encode("utf-8")
            tweetes.append(tokenizer.tokenize(text)[0].encode("utf-8"))
            counter += 1
            if counter % 1000 == 0:
                print "Found %s tweets" % counter

    print "Start feature extraction"
    doNMF(tweetes, n_topics, n_top_words)


def doNMF(dataset, n_topics, n_top_words):
    """Implement NMF algorithm"""
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.decomposition import NMF

    n_features = 10000
    # n_topics = 5
    # n_top_words = 20

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


def readJson(filename):
    T = []
    counter = 0
    print filename
    f = open(filename, "r")
    # get an items
    # for text in ijson.items(f, u"text"):
    print "start loading"
    tweets = json.load(f)
    print "finish loading"
    for tweet in tweets:
        T.append(tokenizer.tokenize(tweet[u'text'])[0].encode("utf-8"))
        counter += 1
        if counter % 1000 == 0:
            print "Found %s tweets" % counter
    print len(T)
    f.close()

    # implement NMF algorithm
    doNMF(T, 10, 10)

if __name__ == '__main__':
    print "this is main"
    # Connect to the database

    readJson("../../output/keyword.json")
    exit()

    client = MongoClient()
    db = client.turkey_withheld_tweets
    collection = db.postall    
    RunMain(collection)
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
# co yeni via erdoğan in izmirli__kemal ta facebook fotoğraf paylaştım

# Topic #1:
# rt mehtapyuceel tanerunal682 orgidee79 için fuatavnifuat türk theredhack akp çok

# Topic #2:
# robyslann porn_christine jennycarlington sexkittinsza orgidee79 melanie_lausa club_eliteza morning good sammier1985

# Topic #3:
# 10 için 12 mi fuatavnifuat 11 ın bugün sonra erdoğan

# Topic #4:
# günaydın mehtapyuceel den ekinmehtap sbstys gktg_ztrk sabahlar hayırlı teşekkürler mutlu




