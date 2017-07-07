import webscraper
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Dictionary(object):

	stop_words = set(stopwords.words("english"))

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

	def filterStopWords(self, sentence):

		words = word_tokenize(sentence)
		filtered_words = set()
		for w in words:
			if w not in Dictionary.stop_words:
				filtered_words.add(w)
		return filtered_words

	# gets the appropriate definition of a word and context
	def getDefinition(self, word, context):
		contextWordSet = self.filterStopWords(context)

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
		def freq_dict_initializer(self):
			freq_dict = {}
			text = webscraper.webscrape(self.word, self.definition)
			words = word_tokenize(text)

			for w in words:
				if w not in Dictionary.stop_words:
					if freq_dict.get(w) is None:
						freq_dict[w] = 1
					else:
						freq_dict[w] += 1

			return freq_dict

		def __init__(self, word, definition):
			self.word = word
			self.definition = definition
			self.freq_dict = self.freq_dict_initializer()