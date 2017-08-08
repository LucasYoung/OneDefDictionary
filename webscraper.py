from bs4 import BeautifulSoup
import urllib
import requests
import aux_nlp
import OneDefDictionary

WORD_INSTANCES = 31
MAX_PAGEVISITS = 50

class MarkovChain:
    def __init__(self):
        self.forwardsTokens = []
        self.backwardsTokens = []

def webscrape(word, partOfSpeech, definition):
    """

    webscrapes Wikipedia until WORD_INSTANCES of word are found
    :return: WORD_INSTANCES of text surrounding each instance found
    """
    # getting query and url
    query = (word+" "+definition).replace(" ", "+")
    url = "https://en.wikipedia.org/w/index.php?title=Special:Search&limit="+str(MAX_PAGEVISITS)+"&search="+query
    #print(url)

    # opening page and parsing html
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    # scraping links
    searchResults = soup.findAll("div", {"class": "mw-search-result-heading"})
    if(searchResults is None):
        print("No search results")
        return definition

    concordances = []

    i=0
    while len(concordances) < WORD_INSTANCES and i < MAX_PAGEVISITS and i < len(searchResults):
        link = "http://www.wikipedia.org/"+searchResults[i].find('a').get('href')
        concordances += scrapePage(link, word)
        i+=1

    return concordances[0 : min(WORD_INSTANCES, len(concordances))]

def scrapePage(url, word):
    """

    :param word: word searched for in page
    :param url: url of page to scrape
    :return: all concordances found
    """

    # getting text
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    text = soup.find("div", {"class": "mw-parser-output"}).get_text()

    tokens = aux_nlp.tokenizeFilter(text)

    # concordances is an array of tuples of words near the target word in both the forward and backward direction
    concordances = []

    # finding the concordances
    while True:
        try:
            index = tokens.index(word)
            concordances.append(
                # wrapping forward concordance and backward concordance in a tuple
                (list(reversed(tokens[index - OneDefDictionary.CHAIN_LENGTH : index])),
                 tokens[index + 1 : index + OneDefDictionary.CHAIN_LENGTH + 1])
            )

            # TODO this is a very inefficient way to iterate
            tokens.pop(index)
        except ValueError:
            break

    return concordances