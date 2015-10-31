keyword = ["140journos", "oyveotesi", "sandikbasindayiz", "trnin oylari", "tutanak", "tutanakno"]


def check(tweet):
	for word in keyword:
		if word in tweet["text"].lower():
			return True
	return False
