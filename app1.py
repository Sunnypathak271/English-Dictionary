
import json
#here we imported the json vocab library created by Manish Pathak
# in the syntax form of python dictionary format
from difflib import get_close_matches

interactive_dictonary = json.load(open("data.json"))
#interactive_dictonary is a global variable.

def translate(word):#word is a local variable
    word = word.lower()#here we chose lower() function because data.json(library) contains lower case letters.This function makes the letters during compilation small or of lower case.
    if word in interactive_dictonary:
        return interactive_dictonary[word]#involved the global variable
    elif len(get_close_matches(word,interactive_dictonary.keys()))>0:
        yn = input("Did you mean %s ?\nIF YES THEN PRESS y ELSE PRESS n:\n " %get_close_matches(word,interactive_dictonary.keys())[0])
        if yn == "y":
            return interactive_dictonary[get_close_matches(word,interactive_dictonary.keys())[0]]
        elif yn == "n":
            return "Please type the word again.\nThe word may not be typed correct."
        else:
            return "the word doesn't exist in dictonary."

    else:
        return "the word doesn't exist in dictonary."

For_word_meaning = input("type the word: ")#for making progarm interactive

output = translate(For_word_meaning)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
