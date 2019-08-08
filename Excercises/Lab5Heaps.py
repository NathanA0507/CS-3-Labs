import math
def parent(i):
    return (i-1)//2

def leftChild(i):
    return 2*i + 1

def rightChild(i):
    return 2*i + 2

def HeapInsert(H,item):
    H.append(item)
    i = len(H)-1
#    print(H)
    while i > 0 and item[2] < H[parent(i)][2]:
        H[i] = H[parent(i)]
        i = parent(i)
    H[i] = item

def ExtractMin(H):
    if len(H) <1:
        return None
    if len(H) ==1:
        return H.pop()
    root = H[0]
#    print("heap, og", H)
    p = H.pop()
    i = 0
    m = math.inf
    minVal = math.inf
    while True:    
        m = math.inf
#        print(H)
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
        print("i", i)
        print("H", H)
        print("P",p)
        print("L",L)
        print("M",m)
        print("minVal", minVal)
        if minVal == p: #  Parent is larger that both children
            break
        elif minVal == L[1]:
            i = leftChild(i)
        else:
            i = rightChild(i)
#    print("End of extract min", H)
    return root  





if __name__ == "__main__":
    heap = []
    a = [1,4,300]
    b = [2,1,500]
    c = [4, 5, 200]
    d = [2, 1, 300]
    e = [1, 2, 100]
    f = [1, 3, 400]
    HeapInsert(heap,a)
    HeapInsert(heap,b)
    HeapInsert(heap,c)
    HeapInsert(heap,d)
    HeapInsert(heap,e)
    HeapInsert(heap,f)
    print(heap)
    
    h = ExtractMin(heap)
    print(h)
    print(heap)
    
    
    
    