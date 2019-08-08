'''
Course: CS2302 Data Structures
Author: Nathan Aun
Assignment: Lab 4 - Hash tables
Instructor: Dr. Fuentes
TA: Ismael Villanueva-Miranda
Date of Last Modification: 7/24/2019 
Purpose of Program: To implement and demonstrate 6 different hash functions to compare
the similarity of two words using NLP(Natural language processing)
 '''
import numpy as np
import time
import math
#word class allows for our hash table to be more organized
class Word(object):
    def __init__(self, L):
        self.word = L[0]
        embedding = np.zeros(len(L)-1, dtype = np.double)
        for i in range(1,len(embedding)):
            embedding[i] = L[i+1]
        self.embedding = embedding

#Our hash table stores word objects in it and hashes by the word
class HashTable(object):
    def __init__(self, size = 101, numItems = 0):
        self.item = np.empty(shape=size, dtype=np.object)
        self.numItems = numItems
        
#read file will read all the lines in the file and return a list, where every element is the word and all 50 embeddings
def readFile(fileName):
    f = open(fileName,"r", encoding ="Latin-1")
    fullFile = f.readlines()
    L = []
    for i in fullFile:
        L.append(i.split(' '))
#        if len(L) == 10000:
#            break
    return L

#given a hash table will find the longest chain in it.
#Longest chain is our worst case insert 
def longestChain(H):
    neg_ones=np.argwhere(H.item == None)
    if len(neg_ones)==0:
        return len(H.item)
    neg_ones=np.append(neg_ones, neg_ones[0]+len(H.item))
    chain_lens = neg_ones[1:]-neg_ones[:-1]-1
    return np.max(chain_lens), chain_lens

#Average chain length will find every chain that exists in the hash table and average them together
def AverageChainLength(L):
    total = 0
    numChains = 0
    for i in L:
        if i != 0:
            total += i
            numChains += 1
    return total / numChains
    
#Determines the load factor of the table, used for resizing purposes
def LoadFactor(H):
    return H.numItems / len(H.item)

#this is a general hash function that will call the correct hash function based on what
#the user input. i is used in the case of collisions
def h(H, word, i, hashNum):
    if hashNum == 1:
        return h1(H,word, i)
    if hashNum == 2:
        return h2(H,word, i)
    if hashNum == 3:
        return h3(H, word, i)
    if hashNum == 4:
        return h4(H, word, i)
    if hashNum == 5:
        return h5(H, word, i)
    if hashNum == 6:
        return h6(H, word, i)
    
#hash function 1 works off word length
def h1(H,word, i):
    return (len(word) + i) % len(H.item)

#hash function 2 works off ascii values of the first character
def h2(H, word, i):
    return (ord(word[0]) + i) % len(H.item)    

#hash function 3 works off ascii values of the first character multiplied by the last character
def h3(H, word, i):
    return (ord(word[0]) * ord(word[-1]) + i) % len(H.item)

#hash function 4 works off the sum of ascii values of all characters in the word
def h4(H, word, i):
    temp = 0
    for j in range(len(word)):
        temp += ord(word[j])
    return (i + temp) % len(H.item)

#hash 5 works by adding the first character, followed by adding every other character multiplied by 255
def h5(H, word, i):
    if word == '':
        return 1
    return (i + (ord(word[0]) + 255*h5(H,word[1:],0))) % len(H.item)

#hash 6 works by mutliplying ascii values of every character in the word
def h6(H, word, i):
    hVal = 1
    for x in word:
        hVal *= ord(x)
    return (i + hVal) % len(H.item) 

#this function is called whenever the load factor of the table reaches >.5
#it creates a temp new hash table of a bigger size and sets the original one to it 
def resize(H, hashNum):
    newSize = len(H.item) * 2 + 1
    H2 = HashTable(newSize)
    for i in H.item:
        if i is not None:
            Insert(H2,i,hashNum)
    H.item = H2.item
    H.numItems = H2.numItems

#insert's an item into a hash table
def Insert(H,word,hashNum):
    if LoadFactor(H) > .5:
        resize(H, hashNum)
    for i in range(len(H.item)):
        pos = h(H, word.word, i, hashNum)
        if H.item[pos] == word:
            break
        if H.item[pos] == None:
            H.item[pos] = word
            H.numItems += 1
            return pos
    return -1    
#find will determine whether or not a word is in the hash table
#if the word is, it will return the index of it in the hahs table
def find(H, word, hashNum):
    Hval = h(H,word, 0,hashNum)
    while H.item[Hval] is not None:
        if H.item[Hval].word == word:
            return Hval
        Hval += 1
    return None

#sim reads a file and compares two words and checks how similar they are
def sim(H, hashNum,fileName):
    f = open(fileName,"r")
    fullFile = f.readlines()
    L = []
    for i in fullFile:
        L.append(i.split(' '))
    for i in L:
        i[0] = i[0].strip()
        i[1] = i[1].strip()
        index1 = find(H,i[0],hashNum)
        index2 = find(H,i[1],hashNum)
        if index1 is None or index2 is None:
            print("one or both words are not in the data set, cannot compare")
        else:
            dotProduct = 0
            magnitude1 = 0
            magnitude2 = 0
            for j in range(50):
                embedding1 = H.item[index1].embedding[j]
                embedding2 = H.item[index2].embedding[j]
                magnitude1 += math.pow(embedding1, 2)
                magnitude2 += math.pow(embedding2, 2)
                dotProduct +=  embedding1 * embedding2
            similarity = dotProduct / (math.sqrt(magnitude1) * math.sqrt(magnitude2))
            print("Similarity", i, "=", similarity)
    
if __name__ == "__main__":
    print("loading, please wait")
    L = readFile("glove.6B.50d.txt")
    wordList = []
    for i in L:
        wordList.append(Word(i))
#        if len(wordList) == 1000:
#            break
    print("done!")
    print("What hash function would you like to use? (note, 1-4 take a very long time to run)")
    userIn = input("1-6: ")
    hashNum = int(userIn)
    if hashNum < 1 or hashNum > 6:
        print("Invalid hash argument, program cannot work")
        quit()
    H = HashTable()
    print("building hash table, this may take some time")
    start = time.time()
    for i in wordList:
        Insert(H,i,hashNum)
    timeTaken = time.time() - start
    print("Table size:", len(H.item))
    print("load factor:", LoadFactor(H))
    longest_chain, chain_lens = longestChain(H)
    print("longest chain:", longest_chain)
    print("Average chain length:", AverageChainLength(chain_lens))
    print("Time taken:", timeTaken)
    start = time.time()
    sim(H, hashNum, "testFile.txt")
    timeTaken = time.time() - start
    print("time taken for comparing words:", timeTaken)