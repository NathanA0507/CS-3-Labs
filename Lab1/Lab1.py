# -*- coding: utf-8 -*-
"""
Course: CS2302 Data Structures
Author: Nathan Aun
Assignment: Lab 1 - Recursion
Instructor: Dr. Fuentes
TA: Ismael Villanueva-Miranda
Date of Last Modification: 6/18/2019
Purpose of Program: This program will, when given a word, return all possible anagrams of that word
"""
import time

#adding all the words in the text file to a new set named "wordBank"
#we need to split at the end in order to make our words comparable to
#one another, since they would otherwise have extra spaces and \n at the
#end
wordBank = set(open('words_alpha.txt').read().split())

#create an empty set so we can later fill it with all the 
#possible permutations of the given input
permutationSet = set() 

#This method recursively adds all possible combinations of a
#given input to our set named "permutationSet"
def permutations(l, stringSoFar):
    if len(l) == 0:
        permutationSet.add(stringSoFar)
    else:
        for i in range(len(l)):
            permutations(l[:i]+l[i+1:], stringSoFar + l[i])



def output():
    userIn = input("Enter a word or empty string to finish: ")
    while userIn != '':
        print('Word:',userIn)
        start = time.perf_counter() 
        permutations(userIn, '') 
        #realWords is our final set that contains all real word combinations
        #of our given input
        realWords = permutationSet.intersection(wordBank)
        print('The word',userIn,'has the following', len(realWords),'anagrams:')
        wordList = sorted(realWords)
        print(*wordList, sep = "\n")
        timeElapsed = time.perf_counter() - start
        print('It took', timeElapsed, 'seconds to find the anagrams')
        permutationSet.clear()
        realWords.clear()
        userIn = input("Enter a word or empty string to finish: ")
    print("Goodybe, Thanks for using this program!")


output()
    