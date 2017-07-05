import OneDefDictionary
import nltk

def main():
    one_def_dictionary = OneDefDictionary.Dictionary()
    one_def_dictionary.addWord("acute", "(of an angle) less than 90")
    one_def_dictionary.addWord("acute", "(of a disease or its symptoms) of short duration but typically severe")
    print(one_def_dictionary.getDefinition("acute", "the angle is acute"))

if __name__ == "__main__":
	main()