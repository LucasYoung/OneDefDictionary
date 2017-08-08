import webscraper
import aux_nlp
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.text import Text
from PyDictionary import PyDictionary

CHAIN_LENGTH = 2

dictionary = PyDictionary()

class Node:
	def trainMarkovChain(self, word, partOfSpeech, definition):
		concordances = webscraper.webscrape(word, partOfSpeech, definition)
		#print(concordances)

		# Markov chain of words immediately preceding target word
		self.backwardChain = []

		# Markov chain of words immediately following target word
		self.forwardChain = []

		# Each is an array of a frequency dictionary
		for i in range(CHAIN_LENGTH):
			self.forwardChain.append({})
			self.backwardChain.append({})

		# training the markov chain
		for tuple in concordances:
			# dereferencing the tuple returned from webscraping
			forwardConcordance = tuple[0]
			backwardConcordance = tuple[1]

			# TODO refactor
			# adjusting frequency dictionaries from each concordance
			for i in range(len(backwardConcordance)):
				word = backwardConcordance[i]
				if(self.backwardChain[i].get(word) is not None):
					self.backwardChain[i][word] += 1
				else:
					self.backwardChain[i][word] = 1

			for i in range(len(forwardConcordance)):
				word = forwardConcordance[i]
				if(self.forwardChain[i].get(word) is not None):
					self.forwardChain[i][word] += 1
				else:
					self.forwardChain[i][word] = 1

	def __init__(self, word, partOfSpeech, definition):
		self.word = word
		self.definition = partOfSpeech+"- "+definition
		self.trainMarkovChain(word, partOfSpeech, definition)

# calculates score for how well a node matches a context
def judge(contextConcordance, node):
	# dereferencing tuple
	forwardConcordance = contextConcordance[0]
	backwardConcordance = contextConcordance[1]

	#print(backwardConcordance)
	#print(node.backwardChain)

	#print(forwardConcordance)
	#print(node.forwardChain)

	score = 0
	for i in range(CHAIN_LENGTH):
		frequency = node.forwardChain[i].get(forwardConcordance[i])
		if frequency is not None:
			score += frequency

		frequency = node.backwardChain[i].get(backwardConcordance[i])
		if frequency is not None:
			score += frequency

	return score

def getDefinitions(word):
	nodes = []

	definitions = dictionary.meaning(word)
	#print(definitions)
	for key, value in definitions.items():
		for definition in value:
			nodes.append(Node(word, key, definition))

	return nodes

# gets the appropriate definition of a word and context
def getDefinition(word, context):
	possibleDefinitions = getDefinitions(word)
	default = possibleDefinitions[0].definition

	try:
		context = aux_nlp.tokenizeFilter(context)
		index = context.index(word)
		contextConcordance = (context[index-2:index], context[index+1: index+3])

		maxScore = 0
		maxNode = None
		for node in possibleDefinitions:
			score = judge(contextConcordance, node)
			if score > maxScore:
				maxScore = score
				maxNode = node

		if(maxNode is not None):
			return word + ": " + maxNode.definition
		else:
			return default

	except ValueError:
		return default

'''
Markov chain approach:
Search definition
Build markov chain for each node from webscraping- look at contexts the word is appearing in.
Each markov chain stems in both directions from the word in a sentence.
Evaluate probability of that context appearing for each node
'''