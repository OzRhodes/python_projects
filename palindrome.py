#Palandrome - A short programme to see if an entered word or phrase is a Palandrome
# It accepts phrases
import os

def palandrome(word):
    palandrome_bool = True

    # remove punctuation from the string
    # define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in word:
        if char not in punctuations:
            no_punct = no_punct + char
    # Make lower case
    no_punct = no_punct.lower()
    #reomve spaces
    no_punct = no_punct.replace(" ", "")
    for l in range(0, len(no_punct)):
        if no_punct[l] != no_punct[len(no_punct)-l-1]:
            palandrome_bool  = False
    return palandrome_bool

os.system('clear') 
word = input("Enter a word you thing is a palandrome: ")

outcome = palandrome(word)
if outcome:
    print("{} is a paladrome". format(word))
else:
    print("{} is not a paladrome". format(word))

