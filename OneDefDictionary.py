import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def filterStopWords(sentence):
	stop_words = set(stopwords.words("english"))
	words = word_tokenize(sentence)
	filtered_words = set()
	for w in words:
		if w not in stop_words:
			filtered_words.add(w)
	return filtered_words

class Dictionary(object):
	def __init__(self):
		self.dictionary = {}

	# adds a node to the dictionary
	def addWord(self, word, definition):
		newNode = self.Node(word, definition)

		if self.dictionary.get(word) is None:
			self.dictionary[word] = [newNode]
		else:
			self.dictionary[word].append(newNode)

	# calculates score for how well a node matches a context
	# score is the number of matches between frequency dict and words in context
	def judge(self, contextWordSet, freq_dict):
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
			return word + " - " + maxNode.definition
		else:
			return None

	class Node(object):

		# needs modifying for actual texts
		def freq_dict_initializer(self, definition):
			return dict.fromkeys(filterStopWords(definition), 1)

		def __init__(self, word, definition):
			self.freq_dict = self.freq_dict_initializer(definition)
			self.word = word
			self.definition = definition