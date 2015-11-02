# -*- coding: utf-8 -*-

keyword_hashtags = ["140journos", "oyveotesi", "sandikbasindayiz", "trnin oylari", "tutanak", "tutanakno"]
# keyword_prisoner = [u"hükümlü​" ​​,​u"mahpus​", u"tutuklu​", u"tutsak​", u"tutsak​", u"hapis​"​, ​u"​cezaevi​"​, ​u"​hapishane​"​, ​u"​kodes​"​, ​u"​hapsetme​"​, ​u"​delik​"​​​​​​,​ u"​hapsetme​"​, ​u"​hapis​"​, ​u"​tutukluluk​"​, ​u"​hapsedilme​"​, u"hapishane​"​, ​u"​cezaevi​"​, ​u"​kodes​"​, ​u"​kafes​",u"kapatılma​"​, ​u"​sınırlama​"​, ​u"​loğusalık​", u"tutuklama​", u"talep​", u"şarj etme​"​, ​u"​suçlama​"​, ​u"​yük​"​​​​​, u"baskı​"​, ​u"​zorlama​"​, ​u"​şantaj​"​, ​u"​tutuklama​"​​]

keyword_apk = ["akp"]
keyword = keyword_hashtags
def check(tweet):
	for word in keyword:
		if word in tweet["text"].lower():
			return True
	return False
