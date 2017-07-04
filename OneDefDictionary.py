import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))

def filterStopWords(sentence):
	words = word_tokenize(sentence)
	filtered_words = {}
	for w in words:
		if w not in stop_words:
			filtered_words.append(w)
	return filtered_words

class Dictionary(object):
	def __init__(self):
		dictionary = {}

	# adds a node to the dictionary
	def addWord(self, word, definition):
		newNode = Node(word, definition)

		if dict.get(word) is None:
			self.dictionary[word] = [newNode]
		else:
			self.dictionary[word].append(newNode)

	# calculates score for how well a node matches a context
	# score is the number of matches between frequency dict and words in context
	def judge(contextWordSet, freq_dict):
		score = 0
		for word in contextWordSet:
			frequency = freq_dict.get(word)
			if frequency is not None:
				score+=frequency
		return score

	# gets the appropriate definition of a word and context
	def getDefinition(self, word, context):
		contextWordSet = filterStopWords(context)

		maxScore = 0
		maxNode = None
		for node in self.dictionary[word]:
			score = self.judge(contextWordSet, node.freq_dict)
			if score > maxScore:
				maxScore = score
				maxNode = node

		if(maxNode is not None):
			return maxNode
		else:
			return None

class Node(object):

	# needs modifying for actual texts
	def freq_dict_initializer(definition):
		return dict.fromkeys(filterStopWords(definition), 0)

	def __init__(self, word, definition):
		self.freq_dict = self.freq_dict_initializer(definition)
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