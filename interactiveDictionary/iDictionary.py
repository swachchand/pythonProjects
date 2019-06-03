'''
Interactive dictionary
this gives more verbose explaination of any words you type in and 
also provides an alternative if you mistype a word
'''


import json
from difflib import get_close_matches

##Global Variable for accessing the data file 
data = json.load(open('Data.json')) 

def translate(w):    
    ##Change lower case for all entered words
    w=w.lower()
    if w in data:
        return data[w]
    #######################################################
    #if user entered "delhi" w.title() will check for "Delhi" 
    #as well and give output accordingly.
    #######################################################
    elif w.title() in data: 
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead: Enter Y  if yes and N if NO:" % get_close_matches(w, data.keys())[0])
        if yn == "y" or yn =="Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn=="n" or yn =="N":
            return "No word exists, please double check it."
        else:
            return "We did not understand the selection criteria choose Y/N"
    else:
        return "The word does not exist, please double check it."

word = input('Enter Word: ')
opt=(translate(word))
##Not display in list mode, so display each value in new line
if type (opt) == list:
    for i in opt:
        print(i)
else:
    print(opt)