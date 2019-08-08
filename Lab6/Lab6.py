'''
Course: CS2302 Data Structures
Author: Nathan Aun
Assignment: Lab 6 - Algorithm Design Techniques
Instructor: Dr. Fuentes
TA: Ismael Villanueva-Miranda
Date of Last Modification:  
Purpose of Program:
 '''
import math 
import numpy as np
import random
import time

#recieves a list of items in [[weight, value],[weight2,value2]] format, a target weight and 0
# and returns the highest possible value from taking items (only taking 1)
def backtracking(items, remainingWeight, currentVal):
    if remainingWeight < 0:
        return -math.inf
    if remainingWeight == 0 or items == []:
        return currentVal
    j = max(backtracking(items[1:], remainingWeight-items[0][0], currentVal+items[0][1]), backtracking(items[1:], remainingWeight, currentVal))
    return j

#Same problem as the last one, except we can take fractions of an item. It finds all the value-weight ratios of the items
#array and sorts via the ratio, then we add them to the knapsack by best ratio until we cannot add a full one. When we can't
#we add whatever fraction of it we can
def fraction(items, weight):
    for i in items:
        ratio = i[1] / i[0]
        i.append(ratio)
    items.sort(key = lambda x: x[2]) 
    val = 0
    while weight > 0 and items != []:
        if weight - items[-1][0] < 0:
            ratio = weight/items[-1][0]
            val += items[-1][1] * ratio
            weight = 0
        else:
            weight -= items[-1][0]
            val += items[-1][1]
            items.pop(-1)
    return val

#Randomly selects a default of 10,000 permutations and finds the best one and the value obtained from it
def randomized(items, weight, amountOfRuns = 10000):
    temp = items
    currVal = -math.inf
    goodPermutation = items
    for i in range(amountOfRuns):    
        currWeight = weight
        val = 0
        temp = np.random.permutation(temp)
        #print(temp)
        i = 0
        while currWeight >= 0 and i < len(temp):
            if currWeight - temp[i][0] < 0:
                if currVal < val:
                    currVal = val
                    #print(goodPermutation)
                    goodPermutation = temp
                break
            if currWeight - temp[i][0] == 0:
                val += temp[i][1]
                if currVal < val:
                    currVal = val
                    goodPermutation = temp
                break
            val += temp[i][1]
            currWeight -= temp[i][0]
            i+= 1
    
    return currVal

#uses dynamic programming to find the best value obtained for every possible weight from 0->weight
def dynamic(items, weight):
    arr = np.zeros(weight+1)
    items.sort(key = lambda x: x[0]) 
    for i in range(len(items)):
        for j in range(items[i][0],len(arr)):
            arr[j] = max(items[i][1] + arr[j-items[i][0]], arr[j])
        #print(arr)
    return arr
  
def generateItems(amount = 100):
  L = []
  temp = []
  for i in range(amount):
    temp = [random.randint(1,100), random.randint(1,1000)]
    L.append(temp)
  return L

if __name__ == "__main__":
    #items = [[6,25],[8,42],[14,65],[18,95],[20,100]]
    #items = [[10,60],[20,100],[30,120]]
    items = generateItems(200)
    print(items)
    maxWeight = 50
    before = time.time()
    print("backtracking best val", backtracking(items,maxWeight,0))
    print("time:", time.time()- before)
    before = time.time()
    #items = [[6,25],[8,42],[14,65],[18,95],[20,100]]
    #items = [[10,60],[20,100],[30,120]]
    print("randomized",randomized(items,maxWeight))
    print("time:", time.time()-before)
    before = time.time()
    print("dynamic",dynamic(items,maxWeight))
    print("time:", time.time() - before)
    before = time.time()
    print("Fraction:",fraction(items,maxWeight))
    print("time:", time.time() - before)