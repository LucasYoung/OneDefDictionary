from bs4 import BeautifulSoup
import urllib
import requests

def webscrape(word, partOfSpeech, definition):
    # getting query and url
    query = (word+" "+definition).replace(" ", "+")
    url = "https://en.wikipedia.org/w/index.php?search="+query

    # opening page and parsing html
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    # scraping links
    searchResults = soup.findAll("div", {"class": "mw-search-result-heading"})
    if(searchResults is None):
        print("No search results")
        return definition

    rope = ""

    for i in range(1):
        link = "http://www.wikipedia.org/"+searchResults[i].find('a').get('href')
        rope += scrapeText(link)

    print(rope)
    return rope

def scrapeText(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    content = soup.find("div", {"class": "mw-parser-output"})
    return content.get_text()

# Google custom search API key: AIzaSyDrGPuNV4MkmBb2Y36uO0e4wMwSC39qjOE
# Search engine ID: 007934509129950526906:j8wgjiqdbhy
'''
def webscrape(word, partOfSpeech, definition):
    query = word+" "+definition
    print(query)
    params = {'key': 'AIzaSyDrGPuNV4MkmBb2Y36uO0e4wMwSC39qjOE', 'cx': '007934509129950526906:j8wgjiqdbhy', 'q': query}
    response = requests.get('https://www.googleapis.com/customsearch/v1?', params=params)
    print(response.json())
    return definition
'''