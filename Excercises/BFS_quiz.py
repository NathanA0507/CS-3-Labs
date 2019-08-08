import numpy as np

def bfs(G, startV):
  Q = [startV]
  path = np.zeros(len(G), dtype = int)-1
  discovered = np.zeros(len(G),dtype = bool)
  discovered[startV] = True
  
  while(len(Q) > 0):
    currentV = Q.pop(0)
    for i in G[currentV]:
      if (not discovered[i]):
        Q.append(i)
        discovered[i] = True
        path[i] = currentV
  return path
  
def dfs(G, startV):
  S = [startV]
  path = np.zeros(len(G), dtype = int)-1
  discovered = np.zeros(len(G),dtype = bool)
  discovered[startV] = True
  
  while(len(S) > 0):
    currentV = S.pop()
    for i in G[currentV]:
      if (not discovered[i]):
        S.append(i)
        discovered[i] = True
        path[i] = currentV
  return path
  
if __name__ == "__main__":
  G = [[1,4],[2,5],[3],[],[1,5,7],[2,6,8],[2,3],[5,8],[6]]
  startV = 0
  print(bfs(G,startV))
  print(dfs(G,startV))
  
  
  
  