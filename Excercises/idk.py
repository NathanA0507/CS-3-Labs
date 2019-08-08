# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:57:33 2019

@author: Natha
"""

import graphs
import math
import numpy as np
#------------
#------------
#------------

#YOU CODE GOES HERE:

#runtime: O(|V|)
def count_edges(G):
  count = 0
  for i in range(len(G)):
    count += len(G[i])
  return count
  
#O(|V| + |E|)
def highest_cost_edge(G):
  highest = [0,0,-math.inf]
  for i in range(len(G)):
    for j in range(len(G[i])):
      if G[i][j][1] > highest[2]:
        highest[0] = i
        highest[1] = G[i][j][0]
        highest[2] = G[i][j][1]
  return highest
  
#O(|V|)
def out_degrees(G):
  arr = np.zeros(len(G))
  for i in range(len(G)):
    arr[i] += len(G[i])
  return arr

#O(|V| + |E|)
def in_degrees(G):
  arr = np.zeros(len(G))
  for i in range(len(G)):
    for j in range(len(G[i])):
      arr[G[i][j]] += 1
  return arr

#O(|V|^2)
def AMtoAL(G):
  AL = []
  for i in range(len(G)):
    AL.append([])
    for j in range(len(G[i])):
      if (G[i][j]):
        AL[i].append(j)
  return AL
  
#O(|E|)
def ELtoAL(G):
  AL = []
  for i in range(len(G)):
    while(len(AL) < G[i][0] + 1 or len(AL) < G[i][1] + 1):
      AL.append([])
    AL[G[i][0]].append(G[i][1])
  return AL

#O(|V|^2)
def AMtoEL(G):
  EL = []
  for i in range(len(G)):
    for j in range(len(G[i])):
        if (G[i][j]):
          EL.append([i,j])
  return EL

#O(|V| + |E|)
def ALtoAM(G):
  AM = np.zeros((len(G),len(G)), dtype = bool)
  for i in range(len(G)):
    for j in range(len(G[i])):
      AM[i][G[i][j]] = True
  return AM

#O(|V| + |E|)
def ALtoEL(G):
  EL = []
  for i in range(len(G)):
    for j in range(len(G[i])):
      EL.append([i,G[i][j]])
  return EL

#O(|E|)
def ELtoAM(G):
  maxVertex = 0
  for i in G:
    if i[0] > maxVertex:
      maxVertex = i[0]
    if i[1] > maxVertex:
      maxVertex = i[1]
  AM = np.zeros((maxVertex+1,maxVertex+1), dtype = bool)
  for i in G:
    AM[i[0]][i[1]] = True
  return AM

def top_sort(G):
    TS = []
    in_deg = in_degrees(G)
    Q = list(in_deg[in_deg == 0])
    while len(Q) > 0:
        TS.append(Q[0])
        u = Q.pop(0)
        for v in G[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                Q.append(v)
    if len(TS) == len(G):
        return TS
    return None

  
if __name__ == "__main__":
    G1 = graphs.random_graph_dir(5,7)
    print("unweighted, directed")
    print(G1)
    print("num edges", count_edges(G1))
    print("out-degrees", out_degrees(G1))
    print("in-degrees", in_degrees(G1))
    G2 = graphs.random_graph_dir_weighted(5,7)
    print("weighted, directed graph")
    print(G2)
    print("src, dest, weight", highest_cost_edge(G2))
    
    mess1 = ALtoAM(G1)
    print("al to am \n", mess1)
    print("am to al", AMtoAL(mess1))
    print("am to el", AMtoEL(mess1))
    
    mess2 = ALtoEL(G1)
    print("al to el", mess2)
    print("el to al", ELtoAL(mess2))
    print("el to am \n", ELtoAM(mess2))
    
    print(top_sort(G1))
    
    
    
    
    
    
    
    