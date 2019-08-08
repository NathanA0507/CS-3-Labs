from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

def dsf(size):
    return np.zeros(size,dtype=np.int)-1
    
def find(S,i):
    # Returns root of tree that i belongs to
    while S[i]>=0:
        i = S[i]
    return i

def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri
        return 1
    return 0 
    
def draw_dsf(S):
    scale = 30
    fig, ax = plt.subplots()
    for i in range(len(S)):
        if S[i]<0:
            ax.plot([i*scale,i*scale],[0,scale],linewidth=1,color='k')
            ax.plot([i*scale-1,i*scale,i*scale+1],[scale-2,scale,scale-2],linewidth=1,color='k')
        else:
            x = np.linspace(i*scale,S[i]*scale)
            x0 = np.linspace(i*scale,S[i]*scale,num=5)
            diff = np.abs(S[i]-i)
            if diff == 1:
                y0 = [0,0,0,0,0]
            else:
                y0 = [0,-6*diff,-8*diff,-6*diff,0]
            f = interp1d(x0, y0, kind='cubic')
            y = f(x)
            ax.plot(x,y,linewidth=1,color='k')
            ax.plot([x0[2]+2*np.sign(i-S[i]),x0[2],x0[2]+2*np.sign(i-S[i])],[y0[2]-1,y0[2],y0[2]+1],linewidth=1,color='k')
        ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
         bbox=dict(facecolor='w',boxstyle="circle"))
    ax.axis('off') 
    ax.set_aspect(1.0)

if __name__ == "__main__":    
    plt.close("all")      
    S = dsf(6)
    print(S)
    draw_dsf(S)
    union(S,0,1)
    print(S)
    draw_dsf(S)
    union(S,2,0)
    print(S)
    draw_dsf(S)
    union(S,4,5)
    print(S)
    draw_dsf(S)
    union(S,0,4)
    print(S)
    draw_dsf(S) 
    union(S,0,3)
    print(S)
    draw_dsf(S)     
    union(S,5,0)
    print(S)
    draw_dsf(S)     
    