import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

#Import data
location = '/Users/marrowgari/tensorflow/pron.txt'
data = pd.read_csv(location, names=('Words', 'Phones'))
words = data['Words']
phones = data['Phones']

#Get unique phones and pronunciation word strings
def get_unique(array):
    ph_string = []
    for phone in phones:
        split = phone.split()
        for each_phoneme in split:
            ph_string.append(each_phoneme)
    unique_values = sorted(set(ph_string))
    return(unique_values)

singletons = get_unique(phones)
print("Number of phones: ", len(singletons))
print("Unique phones: ", singletons)

def get_pronunciation(array):
    each_word = []
    for phone in phones:
        y = phone.upper()
        each_word.append(y)
    return(each_word)

pronunciation = get_pronunciation(phones)
print("Each word: ", pronunciation[:5])

#Create a dictionary of unique phones and words containing phones
def createWordDic(rawPhones, rawWords, wordsData):
    wordDict = {}
    phones = capitalize(rawPhones)
    words = capitalize(rawWords)
    for phone in phones:
        wordDict[phone] = []
        for index, word in enumerate(words):
            wordList = word.split(' ');
            if phone in wordList:
                matchList = wordDict.get(phone)
                matchList.append(wordsData[index])
    return wordDict

def capitalize(oldList):
    newList = []
    for element in oldList:
        newList.append(element.upper())
    return newList

phoneWordList = createWordDic(singletons, pronunciation, words)

#Show amount of words (values) associated with each phone (key)
print("Number of phones --->", len(phoneWordList.keys()),'\n')

for key, value in phoneWordList.items():
    print(key, len([item for item in value if item]))
