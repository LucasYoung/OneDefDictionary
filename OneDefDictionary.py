import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))

oneDefDict = {}

def getDefinition(word):
	node = 
	return node.definition


class Node(object):

	# needs modifying for actual texts
	def freq_dict_initializer(definition):
		words = word_tokenize(definition)
		filtered_words = []
		for w in words:
			if w not in stop_words:
				filtered_words.append(w)
		freq_dictionary = dict.fromkeys(filtered_words, 0)
		return freq_dictionary

	def __init__(self, word, definition):
		self.freq_dict = freq_dict_initializer(definition)
		self.word = word
		self.definition = definition






	

	# each node has a set of words aka the definition
	# each node will have a counter
	# walk through array of nodes comparing words in set to words in context
	# 
	# frequency dictionary holds the frequency that each important word in the context 
	# appears in the context
	#
	# 
	#




