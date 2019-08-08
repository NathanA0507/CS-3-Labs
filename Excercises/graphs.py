# Code to generate and display random graphs 
# using an adjacency matrix representation
# Programmed by Olac Fuentes
# Last modified July 16, 2019
import random
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d

def graphFromFile(fileName):
    try:
        L = [[]]
        f = open(fileName,"r")
        fullFile = f.readlines()
        for i in range(len(fullFile)):
            temp = fullFile[i].split(' ')
            vertex = int(temp[0])
            while vertex >= len(L):
                L.append([])
            L[vertex].append(int(temp[1]))
        return L
    except:
        print("it didn't work lol")



def random_graph(vertices, edges, duplicate=True):
    # Generates random graph with given number of vertices and edges
    # If duplicate is true, each edge is included twice in the list
    # that is, for edge (u,v), u is in G[v] and v is in G[u]
    G = [ [] for i in range(vertices) ]
    n=0
    while n<edges:
        s = random.randint(0, vertices-1)
        d = random.randint(0, vertices-1)
        if s<d and d not in G[s]:
            G[s].append(d)
            if duplicate:
                G[d].append(s)
            n+=1
    for i in range(len(G)):
        G[i].sort()
    return G

def random_graph_dir(vertices, edges):
    # Generates random graph with given number of vertices and edges
    G = [ [] for i in range(vertices) ]
    n=0
    while n<edges:
        s = random.randint(0, vertices-1)
        d = random.randint(0, vertices-1)
        if s!=d and d not in G[s] and s not in G[d]:
            G[s].append(d)
            n+=1
    for i in range(len(G)):
        G[i].sort()        
    return G

def random_graph_dir_weighted(vertices, edges):
    # Generates random graph with given number of vertices and edges
    G = [ [] for i in range(vertices) ]
    Guw =  [ [] for i in range(vertices) ]
    n=0
    while n<edges:
        s = random.randint(0, vertices-1)
        d = random.randint(0, vertices-1)
        if s!=d and d not in Guw[s] and s not in Guw[d]:
            w = random.randint(1, 2*vertices)
            Guw[s].append(d)
            G[s].append([d,w])
            n+=1
    return G

def random_graph_weighted(vertices, edges):
    # Generates random graph with given number of vertices and edges
    G = [ [] for i in range(vertices) ]
    Guw =  [ [] for i in range(vertices) ]
    n=0
    while n<edges:
        s = random.randint(0, vertices-1)
        d = random.randint(0, vertices-1)
        if s!=d and d not in Guw[s] and s not in Guw[d]:
            w = random.randint(1, 2*vertices)
            Guw[s].append(d)
            G[s].append([d,w])
            G[d].append([s,w])
            n+=1
    return G
        
def draw_graph(G):
    fig, ax = plt.subplots()
    n = len(G)
    r = 30
    coords =[]
    for i in range(n):
        theta = 2*math.pi*i/n+.001 # Add small constant to avoid drawing horizontal lines, which matplotlib doesn't do very well
        coords.append([-r*np.cos(theta),r*np.sin(theta)])
    for i in range(n):
        for dest in G[i]:
            ax.plot([coords[i][0],coords[dest][0]],[coords[i][1],coords[dest][1]],
                     linewidth=1,color='k')
    for i in range(n):
        ax.plot([coords[i][0],coords[i][0]],[coords[i][1],coords[i][1]],linewidth=1,color='k')
        ax.text(coords[i][0],coords[i][1],str(i), size=10,ha="center", va="center",
         bbox=dict(facecolor='w',boxstyle="circle"))
    ax.set_aspect(1.0)
    ax.axis('off') 

def draw_directed_graph(G):
    #Draws directed graph represented as an adjacency list
    scale = 30
    fig, ax = plt.subplots()
    for i in range(len(G)):
        for d in G[i]:
            x = np.linspace(i*scale,d*scale)
            x0 = np.linspace(i*scale,d*scale,num=5)
            diff = np.abs(d-i)
            if diff == 1:
                y0 = [0,0,0,0,0]
            else:
                y0 = [0,-6*diff,-8*diff,-6*diff,0]
            f = interp1d(x0, y0, kind='cubic')
            y = f(x)
            s = np.sign(i-d)
            ax.plot(x,s*y,linewidth=1,color='k')
            xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
            yd = [y0[2]-1,y0[2],y0[2]+1]
            yd = [y*s for y in yd]
            ax.plot(xd,yd,linewidth=1,color='k')
        ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')    
        ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
         bbox=dict(facecolor='w',boxstyle="circle"))
    ax.axis('off') 
    ax.set_aspect(1.0)

def draw_directed_weighted_graph(G):
    scale = 30
    fig, ax = plt.subplots()
    for i in range(len(G)):
        for edge in G[i]:
            d = edge[0]
            w = edge[1]
            x = np.linspace(i*scale,d*scale)
            x0 = np.linspace(i*scale,d*scale,num=5)
            diff = np.abs(d-i)
            if diff == 1:
                y0 = [0,0,0,0,0]
            else:
                y0 = [0,-6*diff,-8*diff,-6*diff,0]
            f = interp1d(x0, y0, kind='cubic')
            y = f(x)
            s = np.sign(i-d)
            ax.plot(x,s*y,linewidth=1,color='k')
            xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
            yd = [y0[2]-1,y0[2],y0[2]+1]
            yd = [y*s for y in yd]
            ax.plot(xd,yd,linewidth=1,color='k')
            ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")
        ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')        
        ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
         bbox=dict(facecolor='w',boxstyle="circle"))
    ax.axis('off') 
    ax.set_aspect(1.0)

def draw_weighted_graph(G):
    scale = 30
    fig, ax = plt.subplots()
    for i in range(len(G)):
        for edge in G[i]:                
            d = edge[0]
            if i<d:
                w = edge[1]
                x = np.linspace(i*scale,d*scale)
                x0 = np.linspace(i*scale,d*scale,num=5)
                diff = np.abs(d-i)
                if diff == 1:
                    y0 = [0,0,0,0,0]
                else:
                    y0 = [0,-6*diff,-8*diff,-6*diff,0]
                f = interp1d(x0, y0, kind='cubic')
                y = f(x)
                s = np.sign(i-d)
                ax.plot(x,s*y,linewidth=1,color='k')
                xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                yd = [y0[2]-1,y0[2],y0[2]+1]
                yd = [y*s for y in yd]
                #ax.plot(xd,yd,linewidth=1,color='k')
                ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")
            ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')                
            ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
             bbox=dict(facecolor='w',boxstyle="circle"))
    ax.axis('off') 
    ax.set_aspect(1.0)
    

    

if __name__ == "__main__":  
    
    plt.close("all")   
    G0 = random_graph(5, 1)
    draw_graph(G0)
    print('Unweighted undirected graph')
    print(G0)
    
    G1=random_graph_dir(5,7)
    draw_directed_graph(G1)
    print('Unweighted directed graph')
    print(G1)
   
    G2 = random_graph_weighted(5, 7)
    draw_weighted_graph(G2)
    print('Weighted directed graph')
    print(G2)

    G3=random_graph_dir_weighted(5,7)
    draw_directed_weighted_graph(G3)
    print('Weighted directed graph')
    print(G3)

    G4 = graphFromFile("Graph.txt")
    print(G4)
    
    

    