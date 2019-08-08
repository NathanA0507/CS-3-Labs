'''
link to report: https://docs.google.com/document/d/1f_2ij0A9bN8O1Ijv0eAM_nzhIV-_2kOhZTNZhz2hSZ4/edit?usp=sharing
Course: CS2302 Data Structures
Author: Nathan Aun
Assignment: Lab 5 - Graphs
Instructor: Dr. Fuentes
TA: Ismael Villanueva-Miranda
Date of Last Modification: 7/30/2019 
Purpose of Program: To determine the lowest cost path for a drone to get from one city to another
 '''
import xlrd
import graphs
import numpy as np
import math
import dsf

#reads a spreadsheet and populates two seperate lists with the data
def readSpreadsheet(fileName):
    wb = xlrd.open_workbook(fileName)
    sheet = wb.sheet_by_index(0)
    costs = []
    cities = []
    for i in range(1,sheet.nrows):
        costs.append([])
        for j in range(1,sheet.nrows):
            if sheet.cell_value(i,j) > -1:
                costs[i-1].append([j-1, sheet.cell_value(i,j)])
            
    
    for i in range(1,sheet.nrows):
        cities.append(sheet.cell_value(0,i))
    return costs, cities

#Dijksra will run Dijkstra's algorithm to get the paths from one starting vertex to every other city
def Dijkstra(startV,G):
  visited = [False for v in G]
  dist = [math.inf for v in G]
  path = [-1 for v in G]
  dist[startV] = 0
  while (False in visited):
    smallest = math.inf
    vertex = -1
    for i in range(len(dist)):
      if dist[i] < smallest and visited[i] != True:
        smallest = dist[i]
        vertex = i
    visited[vertex] = True
    for i in G[vertex]:
      edgeWeight = i[1]
      alternativePathDistance = dist[vertex] + edgeWeight
      
      if (alternativePathDistance < dist[i[0]]):
        dist[i[0]] = alternativePathDistance
        path[i[0]] = vertex
  return path, dist

#HandlePaths is used in order to handle the information recieved from readSpreadsheet and make paths out of it. This is where most of the program takes place 
def handlePaths(AL, cities, compWeight = []):
    path = []
    weight = []
    for i in range(len(cities)):
        tempPath, tempWeight = Dijkstra(i,AL)
        path.append(tempPath)
        weight.append(tempWeight)
    for i in range(len(path)):
        for j in range(len(path[i])):
            print("path from", cities[i],"to", cities[j], end = ': ')
            if compWeight == []:
                cost = printPath(cities, j, i, path[i], weight[i])
                if cost != None:
                    print("cost:", cost)
                else:
                    print("no path")
            else:
                cost = printPath(cities, j, i, path[i], weight[i], )
                if cost != None:
                    print("cost:", cost)
                    cost = cost - compWeight[i][j]
                    print("diffence from original route:", cost)
                else:
                    print("No path")
                
        print()
    return weight

#printPath will actually print the path that is taken by dijkstra's algorithm
def printPath(cities, j, i, path, weight):
    if path[j] == i:
        print(cities[i], end = ' ') #depends on what we want to display, if the path contain the og city
        print(cities[j], end = ' ')
        return weight[j]
    elif path[j] == -1:
        return None
    printPath(cities, path[j], i, path, weight)
    print(cities[j], end = ' ')
    return weight[j]
        

#The next few methods were taken from an in-class exercise on heaps in order to make the implementation of prim's algorithm better
#finds the parent of an index in a heap
def parent(i):
    return (i-1)//2
#finds left child of an index
def leftChild(i):
    return 2*i + 1
#finds right child of an index
def rightChild(i):
    return 2*i + 2
#inserts a value in a heap while maintaing heap structure 
def HeapInsert(H,item):
    H.append(item)
    i = len(H)-1
    while i > 0 and item[2] < H[parent(i)][2]:
        H[i] = H[parent(i)]
        i = parent(i)
    H[i] = item
#removes the top value in a heap while maintaining heap structure 
def ExtractMin(H):
    if len(H) <1:
        return None
    if len(H) ==1:
        return H.pop()
    root = H[0]
    p = H.pop()
    i = 0
    m = math.inf
    minVal = math.inf
    while True:    
        m = math.inf
        L = [p]
        if leftChild(i) <len(H):
            L.append(H[leftChild(i)])
            if rightChild(i) <len(H):
                L.append(H[rightChild(i)])
        for j in L:
            if j[2] < m:
                m = j[2]
                minVal = j
        H[i] = minVal
        if minVal == p: #  Parent is larger that both children
            break
        elif minVal == L[1]:
            i = leftChild(i)
        else:
            i = rightChild(i)
    return root   

#prim's algorithm will find the minimum spanning tree for a graph given an adjacency list. 
def primsMinTree(AL):
    forest = dsf.dsf(len(AL))
    AL2 = [[] for i in range(len(AL))]
    heap = []
    vertex = 0
    for i in range(len(AL)-1):
        for j in range(len(AL[vertex])):
            HeapInsert(heap,[vertex] + AL[vertex][j])
        while True:
            pointWeight = ExtractMin(heap)
            if pointWeight == None:
                break
            if forest[pointWeight[1]] == -1 and pointWeight[1] != 0:    
                AL2[pointWeight[0]].append(pointWeight[1:])
                AL2[pointWeight[1]].append([pointWeight[0], pointWeight[2]])
                dsf.union(forest,pointWeight[0],pointWeight[1])
                vertex = pointWeight[1]
                print()
                break
            
    return AL2
        
        


if __name__ == "__main__":
    AL, cities = readSpreadsheet("cities.xlsx")
    #print(AL)
    
    #graphs.draw_weighted_graph(AL)
    originalWeight = handlePaths(AL, cities)
    print()
    minSpanAL = primsMinTree(AL)
    #graphs.draw_weighted_graph(minSpanAL)
    #graphs.draw_directed_weighted_graph(minSpanAL)
    #print(minSpanAL)
    handlePaths(minSpanAL, cities, originalWeight)
    