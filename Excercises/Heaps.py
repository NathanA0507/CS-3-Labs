import numpy as np
import matplotlib.pyplot as plt

def parent(i):
    return (i-1)//2

def leftChild(i):
    return 2*i + 1

def rightChild(i):
    return 2*i + 2

def HeapInsert(H,item):
    H.append(item)
    i = len(H)-1
    while i>0 and item > H[parent(i)]:
        H[i] = H[parent(i)]
        i = parent(i)
    H[i] = item
 
def ExtractMax(H):
    if len(H) <1:
        return None
    if len(H) ==1:
        return H.pop()
    root = H[0]
    p = H.pop()
    i = 0
    while True:
        L = [p]
        if leftChild(i) <len(H):
            L.append(H[leftChild(i)])
            if rightChild(i) <len(H):
                L.append(H[rightChild(i)])
        m = max(L)
        H[i] = m
        if m == p: #  Parent is smaller that both children
            break
        elif m == L[1]:
            i = leftChild(i)
        else:
            i = rightChild(i)
    return root   
    
def draw_heap(H):
    if len(H)>0:
        fig, ax = plt.subplots()
        dh(H,0, 0, 0, 100, 50, ax)
        ax.axis('off') 
        ax.set_aspect(1.0)
        
def dh(H, i, x, y, dx, dy, ax):
    if leftChild(i) < len(H):
        p=np.array([[x,y], [x-dx,y-dy]])
        ax.plot(p[:,0],p[:,1],linewidth=1,color='k')
        dh(H, leftChild(i), x-dx, y-dy, dx/2, dy, ax)
        if rightChild(i) < len(H): 
            p=np.array([[x,y], [x+dx,y-dy]])
            ax.plot(p[:,0],p[:,1],linewidth=1,color='k')
            dh(H, rightChild(i), x+dx, y-dy, dx/2, dy, ax)
    ax.text(x,y, str(H[i]), size=20,
         ha="center", va="center",
         bbox=dict(facecolor='w',boxstyle="circle"))
    
def HeapSort(A):
    H = []
    for a in A:
        HeapInsert(H,a)
    for i in range(len(A)):
        A[-(1+i)] = ExtractMax(H)

def isHeap(H):
    for i in range(len(H)):
        left = leftChild(i)
        right = rightChild(i)
        if left > len(H) or right > len(H):
            break
        if H[i] < H[left] or H[i] < H[right]:
            return False
    return True

#This kinda fits the description of siblink(k) but description might not be accurate
def find(H,k):
    for i in range(len(H)):
        if H[i] == k:
            return i
    return -1

def sibling(H,k):
    if k % 2 == 0:
        s = k-1
    if k % 2 == 1:
        s = k+1
    if s > 0 and s < len(H):
        return s
    else:
        return None
    

def family(H,k):
    idk = 0

#bad implementation rip
def secondLargest(H):
    if len(H) < 2:
        return None
    i = 1
    secondLargest = -1
    while i < 3 and i < len(H):
        if secondLargest < H[i]:
            secondLargest = H[i]
        i += 1
    return secondLargest

def inPath(H,k):
    i = find(H,k)
    while i >= 0:
        print(H[i])
        i = parent(i)
    
def tryReplace(H,k,m):
    i = find(H,k)
    j = parent(i)
    if H[j] > m:
        H[i] = m
        
def sumElements(H,k):
    currSum = 0
    while k >= 0:
        currSum += H[k]
        k = parent(k)
    return currSum
    
def checkHeap(H):
    for i in range(1,len(H)):
        if H[i] > H[parent(i)]:
            return False
    return True

if __name__ == "__main__":           
    plt.close("all")     
    H = []
    A = [2,6,1,5,3,8,4,12,10]
    for a in A:
        HeapInsert(H,a)
        draw_heap(H) 
    print(H)
    draw_heap(H) 
    
    '''while len(H)>0:
        a = ExtractMax(H)
        draw_heap(H) '''
        
    A = [20, 50, 10, 90, 30, 60, 70, 40, 80, 5]
    HeapSort(A)
    print(A)
    print(isHeap(H))
    print(checkHeap(H))
    print(isHeap(A))
    print(checkHeap(A))
    print("sibling", sibling(H,10)) 
    print("Second largest:", secondLargest(H))
    inPath(H,5)
    tryReplace(H,5,4)
    draw_heap(H)
    tryReplace(H,2,10)
    draw_heap(H)
    print('Sum', sumElements(H,5))
    