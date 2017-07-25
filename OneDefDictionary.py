import webscraper
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from PyDictionary import PyDictionary

stop_words = set(stopwords.words("english"))
dictionary = PyDictionary()

def filterStopWords(sentence):

	words = word_tokenize(sentence)
	filtered_words = set()
	for w in words:
		if w not in stop_words:
			filtered_words.add(w)
	return filtered_words

class Node(object):

	# needs modifying for actual texts
	def freq_dict_initializer(self, word, partOfSpeech, definition):
		freq_dict = {}
		text = webscraper.webscrape(word, partOfSpeech, definition)
		#parse words into a set
		words = word_tokenize(text)

		for w in words:
			if w not in stop_words:
				if freq_dict.get(w) is None:
					freq_dict[w] = 1
				else:
					freq_dict[w] += 1

		return freq_dict

	def __init__(self, word, partOfSpeech, definition):
		self.word = word
		self.definition = partOfSpeech+"- "+definition
		self.freq_dict = self.freq_dict_initializer(word, partOfSpeech, definition)

# calculates score for how well a node matches a context
# score is the number of matches between frequency dict and words in context
def judge(contextWordSet, freq_dict):
	score = 0
	for word in contextWordSet:
		frequency = freq_dict.get(word)
		if frequency is not None:
			score+=frequency
	return score

def parseDict(word):
	nodes = []

	definitions = dictionary.meaning(word)
	print(definitions)
	for key, value in definitions.items():
		for definition in value:
			nodes.append(Node(word, key, definition))

	return nodes

# gets the appropriate definition of a word and context
def getDefinition(word, context):
	possibleDefinitions = parseDict(word)
	contextWordSet = filterStopWords(context)

	maxScore = 0
	maxNode = None
	for node in possibleDefinitions:
		score = judge(contextWordSet, node.freq_dict)
		if score > maxScore:
			maxScore = score
			maxNode = node

	if(maxNode is not None):
		return word + ": " + maxNode.definition
	else:
		return None