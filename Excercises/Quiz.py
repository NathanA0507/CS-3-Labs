import graphs
import math

#---------------------------------
#runtime #1: O(1)
def vertices(G):
    return len(G)

#runtime #2: O(|V| + |E|)
def is_isolated(G,v):
  for i in G:
    for j in i:
      if j == v:
        return False
  if len(G[v]) == 0:
    return True
  return False
  
#runtime #3: O(|E|)
def edge_weight(G,u,v):
    item = -1
    for i in range(len(G[u])):
      if G[u][i][0] == v:
        item = i
    if item < 0:
      weight = math.inf
    else:
      weight = G[u][i][1] 
    return weight

#runtime #4 O(|V| + |E|)
def complement(G):
  set1 = set([])
  set2 = set([])
  G2 = []
  for i in range(len(G)):
    set1.add(i)
  for i in G:
    G2.append([])
  for i in range(len(G)):
    set2.add(i)
    for j in range(len(G[i])):
      set2.add(G[i][j])
    G2[i] = list(set1.difference(set2))
    set2.clear()
  return G2


#---------------------------------
#TEST YOUR CODE HERE

#[[1],[0,3,4],[3,4],[1,2],[1,2]] -> [[2,3,4],[2],[0,1][0,4][0,3]]
G  = [[1],[0,3,4],[3,4],[1,2],[1,2]]
print(complement(G))