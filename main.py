import OneDefDictionary
import nltk

def main():
    word = "sow"
    context = "pigs"
    print(OneDefDictionary.getDefinition(word, context))

if __name__ == "__main__":
	main()