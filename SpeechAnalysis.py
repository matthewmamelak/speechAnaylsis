#This program searches through three text files and finds the number of
#characters, sentences, words, unique words, % of unique words and the longest word.
#It also displays a list of the top ten most used words that are over 5 letters long
#Most used 5+ letter word from each speach: Harper's Speech - people, Obama's Inaugural Address - nation, Obama's Berlin Speech - people
#This program is written by Matthew Mamealk for CISC 101 - Due Fri Jun 11, 2021

import collections
from collections import Counter
from collections import OrderedDict

def fileRead(fileName):
    """The function fileRead opens and reads a text file with a specified file name."""
    openFile = open(fileName, "r") #Opens a file stored in the fileName variable
    fileContents = openFile.read()
    openFile.close()
    return fileContents

def textMarkup(listOfStrings):
    """The function textMarkup makes all uppercase letters to lower case.
    It also replaces all double spaces, hypens and linefeeds with a single space."""
    stringFix = " "
    stringHypen = listOfStrings.replace("-", " ") #Replaces a hypen with a space
    stringSpace = stringHypen.replace("\n", " ") #Replaces a new line feed with a space
    for a in stringSpace:
        if a.isalpha() or a == " ":
            stringFix = stringFix + a
    lowerCase = stringFix.lower() #Makes all words lowercase
    while lowerCase.count("  ") > 0: #Replaces a double space with a single space 
        lowerCase = lowerCase.replace("  ", " ")
    return lowerCase
 
def textList(string):
    """The function textList makes the text into a list of words"""
    listOfStrings = [] #Creates an empty tuple
    listOfStrings = string.split() 
    return listOfStrings

def sortList(listOfStrings):
    """The function sortList sorts the list in alphabetical order."""
    listSorted = sorted(listOfStrings) #Sorts the list into alphabetical order
    return listSorted

def uniqueWords(listOfStrings):
    """The function uniqueWords creates a list of unique words and sorts the list in alphabetical order."""
    uniqueWords = set(listOfStrings) #Creates a list of unique words
    uniqueWordsSorted = sorted(uniqueWords) #Sorts the list of unique words
    return uniqueWordsSorted

def sumCharacters(fileInfo):
    """The function sumCharacters counts the number of characters in the file in the form of a list."""
    sumCharacters = list(fileInfo) 
    return sumCharacters

def sumSentances(fileInfo):
    """Finds total number of sentences in the text file by searching for periods,
    exclamation marks, and question marks."""
    symbolA = fileInfo.count("?")
    symbolB = fileInfo.count("!")
    symbolC = fileInfo.count(".")
    sumSentances = symbolA + symbolB + symbolC #Counts the # of .,!,? and determines the total number of sentences
    return sumSentances

def percentUniqueWords(uniqueWordList, cleanList):
    """The function percentUniqueWords calculates the percentage of unique words in the .txt file."""
    everyWord = len(cleanList) #Stores a numeric value for the total # of words
    uniqueWords = len(uniqueWordList) #Stores a numeric value for the total # of unique words
    percentUniqueWords = (uniqueWords / float(everyWord)) * 100.0 #Finds the percentage of unique words
    return percentUniqueWords

def biggestWord(uniqueWordList):
    """The function biggestWord finds the largest word from the unique word list."""
    biggestWord = max(uniqueWordList, key=len) #Finds the longest word using the max function
    return biggestWord

def uniqueWordsDictionary(cleanList, uniqueWordList):
    """The function uniqueWordsDictionary counts the number of unique words
    and creates a dictionary that stores each unique word."""
    dictionary = {}
    wordCount = Counter(cleanList) #Counts number of words in cleanList       
    dictionary.update(wordCount) #Updates the list of words to the dictionary
    return dictionary

def writeDictionary(fileName, fileContents):
    """ The function writeDictionary prints out the contents in the dictionary to a .txt file
    sorted in alphabetical order. """
    newFile = open(fileName, "w")
    dictionarySorted = OrderedDict(sorted(fileContents.items())) #Sorts the dictionary
    for space, newLine in dictionarySorted.items():
        newFile.write(str(space) + " ") #Prints the word 
        newFile.write ("= ")
        newFile.write(str(newLine) + "\n") #Prints the number of occurances
    newFile.close()
    
def wordCount(dictionary):
    """The function wordCount finds all the words that are over 5 letters, sorts them
    from greatest to lowest frequency and returns the top ten most frequent words with over 5 letters"""
    dictionary1 = {} #Creates a dictionary that will store all words with more than 5 letters in it
    for letter_count, storage in dictionary.items():
        if len(letter_count) > 5: #If letter count is greater than 5
            dictionary1[letter_count] = storage #Store this value in dictionary1    
    tenLongWords = sorted(dictionary1.items(), key = lambda x: x[1])[-10:] #Store the top 10 most frequenet 5+ long lettered words
    return tenLongWords
          
def main():
    for listCount in range(3): #For loop that runs 3 times, for 3 speeches.
        try:
            speechList = ("PMHarperBerlinWall.txt", "PresObamaInauguralAddress.txt", "PresObamaBerlinSpeech.txt")
            fileInfo = fileRead(speechList[listCount])
        except ValueError:
            print("ERROR: There was no text found in this file.")
        #The code below reads the speech, and creates a sorted list in a dictionary of each word and their frequency.    
        stringCleanup = textMarkup(fileInfo) 
        cleanedTextList = textList(stringCleanup)
        cleanList = sortList(cleanedTextList)
        uniqueWordList = uniqueWords(cleanList)
        dictionary = uniqueWordsDictionary(cleanList, uniqueWordList)

        #The code below determines the number of characters, sentences, unique word percent and longest word
        #It also display the most frequent words that are over 5 letters long.
        speechDictionary = ("PMHarperBerlinWallDict.txt", "PresObamaInauguralAddressDict.txt", "PresObamaBerlinSpeechDict.txt",)
        nameOfSpeech = ("Harper's Speech: ", "Obama's Inaugural Address: ", "Obama's Berlin Speech: ")
        print(nameOfSpeech[listCount])
        characterCount = sumCharacters(fileInfo)
        print(str(len(characterCount)) + " characters.")
        sentenceCount = sumSentances(fileInfo)
        print(str(sentenceCount) + " sentences.")
        print(str(len(cleanList)) + " words.")
        print(str(len(uniqueWordList)) + " unique words.")
        uniquePercentage = percentUniqueWords(uniqueWordList, cleanList)
        print("{0:2.1f}% of the words are unique.".format(uniquePercentage))
        bigWord = biggestWord(uniqueWordList)
        print("Longest word is: " + bigWord)

        mostUsedWords = wordCount(dictionary) 
        print("\nMost used words over 5 letters are: ")
        for term, appearances in mostUsedWords:
            print(str(term) + ":", str(appearances) +" times")
        print("_" * 40)
        

main()
