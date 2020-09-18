import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def translate(word):
    word = word.lower()
    if word in data: 
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0 :
        res = input("Did you mean %s instead? Enter Y if Yes, or N if No.: " % get_close_matches(word, data.keys())[0])
        res = res.upper()
        if res == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif res == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

print(translate(word))




