import OneDefDictionary
import nltk

def checkInput(word, context):
    # TODO implement
    return True

def main():
    word = "sow"
    context = "The number of pigs a sow can produce annually continues to be a popular measure of production efficiency."
    if(checkInput(word, context)):
        print(OneDefDictionary.getDefinition(word, context))

    word = "acute"
    context = "The angle at the slice's tip is smaller than 90 degrees, making it an acute angle. Kitchen tongs"
    if(checkInput(word, context)):
        print(OneDefDictionary.getDefinition(word, context))

if __name__ == "__main__":
	main()