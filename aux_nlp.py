from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import enchant
import string

stop_words = set(stopwords.words("english"))

def tokenizeFilter(text):
	# tokenize non-punctuation words
	tokens = RegexpTokenizer(r'\w+').tokenize(text)

	# filter stop words, toLowerCase
	filtered_tokens = []
	for w in tokens:
		if w not in stop_words:
			# de-pluralize
			d = enchant.Dict("en_US")
			if(w[len(w)-1] == 's' and d.check(w[0: len(w)-1])): # is it a plural version of an existing word?
				w = w[0: len(w)-1]
			filtered_tokens.append(w.lower())

	# TODO de-pluralize

	return filtered_tokens