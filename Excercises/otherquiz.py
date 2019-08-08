#import graphs # learn more: https://python.org/pypi/graphs
import math
import numpy as np

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
      
print(Dijkstra(0, [[[1,1],[2,4]],[[4,6],[2,2]],[[4,2],[3,4]],[],[[3,1]]]))

