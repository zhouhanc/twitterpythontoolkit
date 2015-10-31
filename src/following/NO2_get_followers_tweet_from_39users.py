#part of the code is credit to thid resource http://coding2day.com/TwitterPython.pdf
"""
    @
    @Description:   This python script retrieves all tweets (up tp 3200) from a list of users
    @               and stores those tweets into a txt file.
    @             
    @Author:        Joe Chen
    @Last modified: 04/30/2015 
"""

import time
import json
import urllib2
import oauth2


# 1)from (r.t)
#consumer = oauth2.Consumer(key="TWRBSpgSMkEjzcdpcyZxBX01X", secret="lyzpMfOfQXi9wzSl2KcPtqtHdcEuklCrAtQBI7y5DdUw1vVS2Q")
#token = oauth2.Token(key="2427867182-uNdht7AKnyBIfovdPP36Ly7QPFxiPYQxDUK9v9M", secret="y8u8Tl0sT1pQHJben60EIpaqVVPcVbDTEQjEpEZVjORiW")

# 2)from Joe Chen
consumer = oauth2.Consumer(key="CuyDAqUbCTF6y6k6mcoGF8owZ", secret="OucJJMnHbYCVNKNgyEJSNBMWBXapwSGuwy1Xc28mXR5vLixrNQ")
token = oauth2.Token(key="1979279791-8qRguXNd21mgHR8khU9hg8rcyXkHHSE65tkwFlv", secret="HIR4DQEyHVPrvXm2XNsTToVcgIgxWM2WR2eOoaY1iJV6R")

# 3)from Joe Chen, another one
# consumer = oauth2.Consumer(key="z4k1E4pOj8ncQ4MAdjY1r1Ty9", secret="92mLHrYChG5sHRdZsUc90JG7RRh8cewrl5Hjf2IoPunCAL8HRz")
# token = oauth2.Token(key="1979279791-tSDamC8WUIxU9Z8uFnkWe5eLNSUlGYhGu8l5zZ1", secret="FNMSlsqgcIRmjeCf0BqD9TamwAD1ZfMC77n0x0cOpsICZ")

# 4) name: summer research project
# consumer = oauth2.Consumer(key="Vsj9hKjxGPk4JxBj4al3i7JHX", secret="TbPwe5ltq7U4GtaeMtUhyMxxYb6jNvgyXWZsGsjKqcxbZCFhbD")
# token = oauth2.Token(key="1979279791-c9yR5GJlLrg78jTIifIckvllZf8NBRl8K5aU8OZ", secret="FHuPvdPcbU3Xu77I44pqc64FmLGh82Bkftgq0xwqmRHhR")
#resource https://dev.twitter.com/rest/reference/get/statuses/user_timeline 

# 5) another one from (r.t)
# consumer = oauth2.Consumer(key="7UdhFCq7yb4mA4li0oALa21gY", secret="T9mi5ncQYvzG7BJTULg7HMu6JtCO9dKuFRBf27hphADmqSY5Dp")
# token = oauth2.Token(key="2427867182-uAO0GYXdCma0lHHAYEFZ7xsh2Q4RgKczAGEQ0XM", secret="uszLj4dpKqqDZZq8MZzpHPWxJ8xYrFqhQbfXl48iYjlFR")


APIUrl='https://api.twitter.com/1.1/statuses/user_timeline.json'


## this is the complete list of users (632 users currently)
##userlist = [210913570, 144910421, 2306253432, 2560901623, 2354804863, 2567892499, 2934447874, 831042170, 1860629066, 1333689841, 149944117, 1495389804, 1604469463, 2221420291, 2384992934, 2830018971, 2190994886, 2344755087, 1192784568, 2872713657, 266391875, 960475207, 98559573, 2459516192, 2394065131, 1516382378, 2369675152, 2335356522, 2262648341, 1551131594, 1530559357, 539775766, 543746139, 2388560971, 400592971, 2849867709, 1015031731, 287872926, 2233501515, 866234136, 209022702, 1524584124, 247910015, 893152885, 129435199, 1589509646, 1045431788, 274921047, 338767312, 2413735258, 2299904540, 90000530, 332942376, 1013766662, 63108096, 98561020, 468294583, 378542950, 2457869128, 1608504102, 2173524766, 142617295, 358724726, 2515313327, 2212217482, 1858781809, 2343496301, 300110444, 164207206, 1300533830, 1389142550, 571095572, 126097932, 227275128, 809505068, 412606729, 1665795456, 144740580, 178508146, 360544307, 177526815, 2372427774, 420542453, 943618561, 191152113, 2216746988, 185149415, 1533929442, 709555194, 260293967, 2229813207, 354574294, 186048246, 1534281679, 2320474061, 415807433, 368533448, 372424647, 1708412870, 2149695422, 300857275, 97388474, 248551353, 2179975096, 181381041, 567476141, 571893672, 1585530770, 394143630, 1287182316, 247234439, 239560573, 235593590, 190971758, 234764125, 379247247, 768616170, 2248863568, 2187923278, 1456806882, 1064245063, 2345135930, 211666738, 1666021746, 2264624936, 59168551, 2170087205, 823516964, 172666657, 892690208, 349222687, 2568273694, 420622105, 2306250518, 1050995641, 361103106, 360079105, 108529408, 2473449209, 2924472055, 382633718, 1490120436, 354629362, 271455984, 1879107308, 266137323, 98686698, 999818984, 1336157924, 197390048, 78896862, 284659420, 826087129, 840378072, 303992535, 2655198499, 1505077880, 1710167760, 1155724237, 266088834, 201815756, 398249591, 160235185, 2577122989, 1083948716, 574569414, 2200082083, 2562946722, 2435298974, 1479257756, 277977240, 1096976022, 637052561, 1166313104, 1071777422, 290068103, 2366047872, 466585213, 381590121, 538054259, 1047704508, 966759355, 1409625698, 740136542, 998811228, 156252540, 230499257, 2451844692, 344061522, 2367444561, 2282298960, 471924302, 1543567970, 541066824, 62379586, 2732543552, 91805243, 234053178, 228099630, 944018012, 471557670, 239466019, 322575899, 170743321, 142360088, 1633547796, 1640656400, 2458275339, 302001665, 1016026620, 2499870198, 1142083058, 1052966384, 2303159784, 274915921, 2330836446, 865060315, 265795023, 2386980300, 335529419, 1959411144, 1901110724, 1539272131, 56370624, 1498504639, 970714556, 1489608120, 2616229790, 2278718899, 573457840, 1606491566, 285685164, 590828971, 389287334, 2849619365, 2380580252, 712078746, 2402829718, 1549223150, 97633683, 179017103, 2253026699, 160658789, 569802117, 76805507, 463269249, 1461974400, 1443575359, 2302825842, 99064291, 124790124, 577117546, 276720999, 466883941, 1683467618, 395306554, 2517059812, 2427153746, 1557767503, 316374349, 2289333578, 2201374022, 162489668, 493159745, 2200341824, 400627004, 1732820281, 111437703, 208144603, 74941726, 363033884, 445021463, 2342114582, 173522191, 190567693, 528447703, 541785347, 2229724417, 1967271168, 440917246, 311561469, 921134328, 891131125, 2479793396, 319032563, 2371738866, 215379182, 121474284, 1141056037, 96951518, 738335964, 1863783642, 305603793, 214252752, 2196528330, 941335753, 405890248, 143902581, 1628015804, 489213114, 461970617, 1368171702, 104248495, 200934574, 1114797229, 760305271, 187853991, 2152973473, 478807196, 153871515, 369721198, 574788539, 2205013128, 2375713921, 1707920508, 988206198, 269739120, 93713515, 1267565670, 280925274, 2545056857, 33021011, 1705022546, 386260046, 632042571, 551765066, 1040443916, 300792901, 1634131010, 83117119, 895867956, 215108651, 1567759398, 183263067, 2516663327, 2712028184, 169567253, 234464275, 491439959, 329783809, 967918597, 2569335802, 216703991, 715729747, 2167098348, 360877030, 328580066, 2728149981, 214895579, 603147226, 2501182422, 1344397134, 1609184210, 267322321, 960730062, 104778701, 292221431, 185216754, 337820614, 139162102, 1519772605, 802849724, 236587963, 637227961, 296082356, 2495015859, 1926028202, 351562665, 179497894, 485143460, 290093985, 64699295, 282129300, 2756541331, 300211090, 347468689, 634495868, 444099447, 1172145013, 2286444007, 2237602665, 2424552293, 211807076, 937657183, 1372470992, 2311924567, 1621328726, 575607267, 962642744, 133405519, 1311720270, 302222142, 943086397, 808385336, 1522123574, 426980149, 544637743, 1594420009, 1059314468, 2402033341, 608365343, 316361499, 1684722458, 968925972, 2203513476, 87440144, 275143438, 1584018188, 1855773446, 2223434499, 1583069954, 1086345344, 159240960, 2433391358, 1634079482, 2152649513, 378610418, 342590193, 415589102, 372746988, 483085035, 2261181162, 1596081276, 419056358, 1568086754, 2162295521, 604512990, 2362958557, 331811548, 2382625499, 1516251860, 1566231246, 302566092, 160647879, 109233611, 2268749940, 951806646, 1492581044, 216545966, 291932843, 208304800, 1126292118, 295701955, 1927671576, 1583321732, 360475264, 289639038, 550390397, 175452791, 941318774, 2368859503, 745302638, 736508521, 261438051, 148509282, 2491202142, 2417707450, 144460380, 1626471854, 327852625, 270404176, 610210382, 2523392589, 1648456268, 2507928133, 329011778, 137609792, 2697804350, 344962488, 1357677115, 2264320568, 384786997, 2513387953, 238582534, 323379742, 1079298589, 944015900, 334641685, 2260670982, 2374365700, 2348577281, 326605309, 602198524, 815096310, 943466988, 372373987, 2779830754, 514769377, 72402341, 357147102, 1600541148, 385868250, 310739417, 49134040, 314411472, 2503887309, 853354956, 1307185572, 360509898, 69073349, 2348321218, 49115578, 2280628662, 271946163, 2298110385, 378538413, 1571635627, 69083561, 201195941, 1079310756, 454945171, 574755217, 99264910, 375079308, 1498263942, 909001092, 2386010498, 1627644289, 2205712106, 2400737660, 2453686650, 191203703, 1147345266, 1521887600, 1833128298, 375077217, 247212384, 594504031, 2203588955, 352215385, 1901615448, 811186411, 136403283, 1183500626, 877123920, 1475500364, 559892809, 1337342689, 1683884358, 1482768709, 166279488, 300733150, 247542067, 2508060974, 1718714666, 349114660, 288327971, 1831459106, 2264973360, 105771292, 1851529494, 159293715, 547094232, 434121090, 1917329670, 379070723, 190718205, 1574779604, 944075000, 2209198321, 1919670511, 14612713, 446220519, 425388262, 1243806758, 1633200354, 1580830945, 2320849116, 569307355, 870709464, 2451402967, 149424333, 475141495, 97286346, 1655265480, 719849671, 2367912133, 946428098, 83155133, 1144602812, 374950073, 615231669, 1338706099, 246689968, 333521071, 63538506, 1049567401, 524413095, 633997467, 917790872, 720449686, 738879636, 1634107538, 94433424, 808018062, 279732361, 1241081988, 527114371, 131647618, 1628692596, 295391343, 1249247334, 72210532, 601890915, 1711630434, 183629919, 105797726, 2442543195, 777683034, 2273362006, 310896722, 2318784593, 1015074896, 2424068175, 2236780618, 543447112, 2356578372, 33235009, 2509524427, 700614704, 740397097, 1277114408, 108714019, 1050361886, 1093250394, 955867160, 1172965398, 808771604, 264137048, 309880847, 2339233804, 1210492932]
userlist =  [2730091235, 2725839665, 1513923781, 2423539531, 2722883572, 159849067, 2614605146, 1272813649, 2651815323, 2570895621, 2312887871, 2476132093, 2606729093, 456744981, 476704359, 2261869896, 2464343782, 2526154078, 1788492714, 2513272767, 2508488495, 1622770908, 970968402, 2437789101, 2465999297, 2446855651, 1474483226, 2479375781, 2384966539, 2373640023, 2394529924, 2336362912, 2401019043, 2275455587, 2399965393, 2399223764, 2415883281, 2411976543, 2407747715, 2196068223, 2386479566, 2403590595, 1593227276, 2382384901, 2370300535, 483146248, 2370469348, 2375924534, 2388990208, 2371885483, 2343091251, 2241864915, 2166605717, 2356578770, 2356654933, 822848173, 2235824184, 2353338328, 2339864615, 1573531832, 2245006277, 2347305164, 2346827301, 2345576655, 2345425479, 2345185374, 2303576306, 2343575124, 2343328795, 2342650404, 2342147122, 2342192875, 2165232541, 2338936478, 2328211721, 2333036489, 2334179579, 160518396, 2324265249, 2305185362, 78559428, 2307148550, 496101465, 2314447816, 2190298869, 2317883737, 1332771931, 1698573156, 2310691861, 2291779257, 268017380, 2198515187, 2302013533, 166789644, 2297997163, 1473493369, 2286512038, 2293125804, 2239937911, 2222374727, 2291517146, 2290106798, 2287102272, 2288772560, 2275352512, 468781263, 840540392, 233913860, 2262736570, 2276677237, 2258477949, 2250795732, 612011220, 1615292581, 2236354380, 1855314980, 2266419259, 2268725089, 1700374796, 2267877290, 2261387912, 2244647453, 1630675585, 2261944538, 928301418, 2258326183, 2261135574, 1351873987, 2160925097, 2251206883, 706101323, 111437703, 2389868851, 2388829896, 2385460214, 2373423080, 2333939449, 2281806576, 1709373745, 91634935, 3093155938, 3082569536, 2876830371, 3014780001, 2974969569, 2581537049, 1594322090, 2279369159, 428384431, 2471663717, 2337707476, 2432158945, 2455563389, 2428923391, 2458631452, 2423731609, 106396709, 2414944523, 2427839631, 2401558796, 1392660672, 2399938062, 2398130634, 2415871947, 2305664169, 2381053165, 2389818320, 2409068043, 2405546194, 2332615746, 2399532957, 1115303442, 2391078333, 2374076627, 2364544124, 2359847142, 2266552116, 2357019718, 2335719767, 2354564270, 2348474965, 2347303661, 2246126863, 2344772597, 2312790401, 2156271249, 2322219559, 2329909772, 2313501690, 2327679103, 2326236247, 2313153651, 2317545348, 2310066653, 2311822862, 1649330592, 1272237974, 402849480, 2208977420, 2304500897, 2310818658, 2294831072, 2304178252, 2303360866, 2306452014, 2279624687, 2302458109, 1670307560, 2282361896, 1573624153, 2292380659, 2285745488, 2223691149, 2269703987, 2265585837, 2277592626, 769044606, 2261760701, 2249816927, 2273088350, 2256447917, 2268774924, 2255231063, 2269206553, 2260928803, 2241777923, 2243699561, 2189931127, 2259043284, 1898690768, 2235177628, 272428730, 2252491824, 2227575327, 2248803396, 2221756048, 1099431157, 2231667535, 2231604818, 2230376036, 2227003830, 2226967572, 2204692683, 2225445385, 2224885640, 2222941322, 2174782949, 2217636685, 2217556232, 2193840904, 2215764920, 2214102750, 2213868764, 2194443203, 2212583809, 2166492922, 2189374515, 1616100318, 2207202140, 1394046558, 2205293090, 739328750, 996479161, 2185033085, 2190008227, 2182849487, 1080491035, 2157598959, 2147693828, 2156838698, 2151155764, 2151108625, 2150693653, 2148586738, 1974163225, 1971207697, 1344862892, 608033172, 1959115027, 1958688474, 1955924587, 706823524, 309028342, 370198022, 1947722293, 1947451267, 703201360, 1938790614, 1921217815, 1913975803, 1904762778, 1904283800, 1882735075, 1831925018, 473945794, 199623237, 1879913000, 1871720311, 1653418908, 323353537, 758804988, 1865325666, 816970388, 1522604234, 1854086558, 1856278716, 1615151665, 1755036230, 1740262160, 1678355190, 1462051370, 1724817122, 1721486125, 450764691, 381408139, 1693767666, 540121201, 810388098, 1702036142, 1700204035, 1699572841, 1647914700, 1693614590, 1692024986, 1688913032, 1562931313, 240448702, 1686207002, 1685832882, 1685704249, 1685595158, 1684315285, 1683610747, 1679162750, 1653509844, 1677677047, 1676372083, 1662343418, 1670944639, 395156477, 1672808400, 1671166033, 1505966378, 1650332923, 1664202702]



## because json.dump can be called only once, ALL_data is a list that stores all tweets
ALL_data = []
#params["screen_name"] ="" #optional
withheld_flag = False


def findprotected():
    """
    This function finds all users that have "true" in their protected field
    
    @inputs: None
    @outputs: None

    """   
    removeUser = ""
    count = 0
    for user in userlist:
        print "current user is ", user
        url = APIUrl
        params = {"oauth_version":"1.0","oauth_nonce": oauth2.generate_nonce(),"oauth_timestamp":int(time.time())}
        params["user_id"] = user
        params["count"] = 2
        params["exclude_replies"] = "true"
        params["oauth_consumer_key"] = consumer.key
        params["oauth_token"] = token.key
        try:
            req = oauth2.Request(method="GET", url=url, parameters=params)
            signature_method = oauth2.SignatureMethod_HMAC_SHA1()# HMAC, twitter use sha-1 160 bit encryption
            req.sign_request(signature_method, consumer, token)
            headers = req.to_header()
            url = req.to_url() 
            response = urllib2.Request(url)
            data = json.load(urllib2.urlopen(response)) #format results as json
            time.sleep(5)
        except Exception, e:
             count += 1
             print user
             print e
             removeUser = removeUser +  str(user) + ", "
        finally:
            pass
    print "number of removed user is ", count
    print " finish scanning, remove those users "
    print removeUser


def get200(user):
    """
    This function gets the first 200 tweets from a user 
    
    @inputs: None
    @outputs: string "stop" if the user has less than 200 tweets, 
              otherwise return the last tweet ID

    """
    url = APIUrl
    params = {"oauth_version":"1.0","oauth_nonce": oauth2.generate_nonce(),"oauth_timestamp":int(time.time())}
    params["user_id"] = user
    params["count"] = 200
    #params["exclude_replies"] = "true"
    params["oauth_consumer_key"] = consumer.key
    params["oauth_token"] = token.key
    
    req = oauth2.Request(method="GET", url=url, parameters=params)
    signature_method = oauth2.SignatureMethod_HMAC_SHA1()# HMAC, twitter use sha-1 160 bit encryption
    req.sign_request(signature_method, consumer, token)
    headers = req.to_header()
    url = req.to_url() 
    #print "get200 url: ", url
    response = urllib2.Request(url)
    data = json.load(urllib2.urlopen(response)) #format results as json
    data_to_store = []

    # store only withheld tweets
    for each_tweet in data:
        if "withheld_in_countries" in each_tweet:
            data_to_store.append(each_tweet)
    print "find " + str(len(data_to_store))  + " new withhled tweets" 

    global ALL_data
    ALL_data = ALL_data + data_to_store

    print "length of data in get200 is", len(data) 
    if len(data) == len(data_to_store) and len(data_to_store) != 0:
        global withheld_flag
        withheld_flag = True

    time.sleep(5) 
    if (len(data) < 100 ):   
        #json.dump(ALL_data, outfile, sort_keys = True, indent = 4)
        #outfile.close()
        return "stop", user
    else:
        return data[len(data)-1][u'id'] - 1, user

def repeat200(first_id, user):
    """
    This function repeatedly search for next 200 tweets of a certain user
    by updating params["max_id"] in timeline API

    @inputs: beginning tweet ID, or string "stop" if no ID is required
    @outputs: None

    """

    if first_id == "stop":
        return
    prev_id = first_id
    #outfile = open("Censoreduser.txt", "a")   
    while True:
        params = {"oauth_version":"1.0","oauth_nonce": oauth2.generate_nonce(),"oauth_timestamp":int(time.time())}
        url = APIUrl
        params["user_id"] = user
        params["count"] = 200
        #params["exclude_replies"] = "true"
        params["max_id"] = str(prev_id)
        params["oauth_consumer_key"] = consumer.key
        params["oauth_token"] = token.key

        req = oauth2.Request(method="GET", url=url, parameters=params)
        signature_method = oauth2.SignatureMethod_HMAC_SHA1()# HMAC, twitter use sha-1 160 bit encryption
        req.sign_request(signature_method, consumer, token)
        headers = req.to_header()
        url = req.to_url()
        #print "repear200 url: ", url 
        response = urllib2.Request(url)
        data = json.load(urllib2.urlopen(response)) #format results as json
        data_to_store = []
        print "length of data of current repeat200 is --> ", len(data)
        # store only withheld tweets
        for each_tweet in data:
            if "withheld_in_countries" in each_tweet:
                data_to_store.append(each_tweet)
        #print "find " + str(len(data_to_store))  + " new withhled tweets" 

        global ALL_data
        ALL_data = ALL_data + data_to_store

        global withheld_flag
        if len(data) != 0:
            if (len(data) == len(data_to_store) ):    
                withheld_flag = True
            else:
                withheld_flag = False

        #for entry in data:
        #    ALL_data.append(entry)  # merge two lists

        time.sleep(5)
        if len(data) < 100:
            #json.dump(data, outfile, sort_keys = True, indent = 4)
            break;
        else:
            prev_id = int(data[len(data)-1][u'id']) - 1

    # json.dump(ALL_data, outfile, sort_keys = True, indent = 4)
    # outfile.close()    


def searchUser(mylist):
    """
    This function gets all tweets from all users in userlist

    @inputs:  a list of userIDs (if you want to search only one user at index i, 
              the input should look like list[i:i+1])
    @outputs: None   
    
    """
    count = 1
    for user in mylist:
        print  "current user id is ", user
        print "this is the " + str(count) + "th user----++++++" 
        count += 1
        try:
            first_id, user = get200(user)
            repeat200(first_id, user) 
        except Exception, e:
            print "got an Exception"
            print e
            # write protected user ID to a seperate file 
            print str(user), " is a protected user ###########"
            outfile_protected.write( str(user)  + " \n")  # python will convert \n to os.linesep
        finally:
            print "finish searching user ", user
            if withheld_flag:
                print str(user), " is a withheld user ###########"
                outfile_withheld.write( str(user)  + " \n")
            else:
                print str(user), " is not a withheld user" 

            # set withheld_flag to false again
            global withheld_flag
            withheld_flag = False    
            print "============================================="
        #first_id="stop"
    # is there another way other than dumping all json data into file in one call?   
    json.dump(ALL_data, outfile, sort_keys = True, indent = 4)
    # close all files
    outfile.close() 
    outfile_protected.close()
    outfile_withheld.close()

    print "finish searching all users"
    print "===================================================="

def load_file(filename):
    """
    A helper function that returns an iterable object

    """
    inputJson=open(filename, "r").read()
    jsonFields=json.loads(inputJson)
    #tweets_count=+len(jsonFields)
    
    return jsonFields

def printWithheld(filename):
    """
    Print the number of tweets that have withheld_in_countries fields

    """

    tweets=load_file(filename)
    print "total number of tweets is ", len(tweets)
    i=0
    for t in tweets:
        if "withheld_in_countries" in t:
            #print t["withheld_in_countries"]
            i+=1
    print "total number of withheld_in_countries tag is " ,i
    print "================================================="

if __name__ == '__main__':
    #tweets=load_file("userTurkeyDEcasestudy1.txt")
    print len(userlist)
    """
    NOTICE:
        After searching several users, the json data received from Twitter becomes empty
        eg. try searchUser(userlist[6:7]) and searchUser(userlist[3:7]), 
        and user id 2934447874 has different results.
    """

    """ IMPORTANT !!! """
    FILE_NAME = "16000_32000"
    ## open a new file
    outfile = open(FILE_NAME + ".txt", "w")
    outfile_protected = open(FILE_NAME + "_protected_user.txt", "w")
    outfile_withheld = open(FILE_NAME + "_withheld_user.txt", "w")

    searchUser(userlist)           # for testing purpose, pick up a random user
    printWithheld(FILE_NAME + ".txt")







