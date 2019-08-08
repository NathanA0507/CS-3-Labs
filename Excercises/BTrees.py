# Code to implement a B-tree 
# Programmed by Olac Fuentes
# Last modified June 28, 2019

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Search(T, k):
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    #Not the best way to implement it
    '''i = 0
    while k > T.item[i]:
        i+=1
        if k == T.item[i]:
            break  or'''
    i = FindChild(T,k) #This one line replaces all the commented section above
    return Search(T.child[i],k)

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
     
def Height(T):
    if T.isLeaf:
        return 0
    return 1 + Height(T.child[0])    
    
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
            
def Smallest(T):
    if T.isLeaf:
        return T.item[0]
    return Smallest(T.child[0])

def Largest(T):
    if T.isLeaf:
        return T.item[len(T.item) - 1]
    return Largest(T.child[len(T.child) - 1])

def NumItems(T):
    if T.isLeaf:
        return len(T.item)
    s = len(T.item)
    for c in T.child:
        s += NumItems(c) 
    return s

def LargestAtDepth(T, d):
    if d == 0:
        return T.item[len(T.item)-1]
    return LargestAtDepth(T.child[len(T.child)-1], d-1)

def max_at_d(T,d):
    if d == 0:
        return T.item[-1]
    if T.isLeaf:
        return 0
    return max_at_d(T.child[-1],d-1)

def count_items(T,d):
    if d == 0:
        return len(T.item)
    if T.isLeaf:
        return 0
    temp = 0
    for i in T.child:
        temp += count_items(i,d-1)
    return temp
        
#Draft one of this method, its a huge mess but it technically works
'''def FindDepth(T, k):
    if T.isLeaf:
        for i in range(len(T.item)):
            if T.item[i] == k:
                return 0
        return -1
    for i in range(len(T.item)-1):
        if k == T.item[i]:
            return 0
        if k < T.item[i]:
            temp = FindDepth(T.child[i],k)
            if temp == -1:
                return -1
            return 1 + temp
        elif k > T.item[i] and k < T.item[i+1]:
            temp = FindDepth(T.child[i+1],k)
            if temp == -1:
                return -1
            else:
                return 1 + temp
    if k > T.item[len(T.item)-1]:
        temp = FindDepth(T.child[len(T.child)-1],k)
        if temp == -1:
            return -1
        else:
            return 1 + temp
    if k < T.item[len(T.item)-1]:
        temp = FindDepth(T.child[0],k)
        if temp == -1:
            return -1
        else:
            return 1 + temp
    if k == T.item[len(T.item)-1]:
        return 0'''
        
def FindDepth(T, k):
    if k in T.item:
        return 0
    if not T.isLeaf:
        i = FindChild(T, k)
        temp = FindDepth(T.child[i], k)
        if temp != -1:
            return temp + 1
    return -1 

def PrintAtDepth(T,d):
    if d == 0:
        print(*T.item, end = ' ')
    elif T.child is None:
        return None
    else:
        for i in range(len(T.child)):
            PrintAtDepth(T.child[i],d-1)
            
def NumLeafs(T):
    if T.isLeaf:
        return 1
    temp = 0
    for i in range(len(T.child)):
        temp += NumLeafs(T.child[i])
    return temp

def FullNodes(T):
    if T.isLeaf:
        if len(T.item) == T.max_items:
            return 1
        return 0
    temp = 0
    if len(T.item) == T.max_items:
        for i in range(len(T.child)):
            temp += FullNodes(T.child[i])
        return temp
    for i in range(len(T.child)):
        temp += FullNodes(T.child[i])
    return temp

def PrintDescending(T):
    if T.isLeaf:
        t = len(T.item) -1
        while t >= 0:
            print(T.item[t],end=' ')
            t -= 1
    else:
        PrintDescending(T.child[len(T.item)]) 
        i = len(T.item) - 1
        while i >= 0:
            print(T.item[i],end=' ')
            PrintDescending(T.child[i])
            i -= 1

#Draft one of this method, its a mess
'''def PrintItemsInNode(T,k):
    found = False
    if T.isLeaf:
        for i in range(len(T.item)):
            if T.item[i] == k:
                found = True
                break
        if found:
            print(*T.item)
            return None
        print("Did not find item", k)
        return None
    for i in range(len(T.item)-1):
        if k == T.item[i]:
            found = True
            break
        elif k < T.item[i]:
            PrintItemsInNode(T.child[i],k)
        elif k > T.item[i] and k < T.item[i+1]:
            PrintItemsInNode(T.child[i+1],k)
    if k == T.item[len(T.item)-1]:
        found == True
    if found:
        print(*T.item)
        return None
    if k > T.item[len(T.item)-1]:
        PrintItemsInNode(T.child[len(T.child)-1],k)
    if k < T.item[len(T.item)-1]:
        PrintItemsInNode(T.child[0],k) '''
        
def PrintItemsInNode(T,k):
    if k in T.item:
        print(*T.item)
        return None
    if not T.isLeaf:
        i = FindChild(T, k)
        PrintItemsInNode(T.child[i], k)

    


if __name__ == "__main__":        
    L = [6,3,16,11,7,17,14,8,5,19,15,1,2,4,18,13,9,20,10,12,21]
    
    T = BTree()    
    for i in L:
        print('Inserting',i)
        Insert(T,i)
        print('Tree structure')
        PrintD(T,'') 
    
    print('Keys in the tree: ')
    Print(T) 
    print()
    print('Tree structure')
    PrintD(T,'') 
    print("Smallest: ", Smallest(T))
    print("Largest: ", Largest(T))
    print("Number of items in the list: ", NumItems(T))
    print("Largest item at depth 1: ", LargestAtDepth(T, 1))
    print("largest item at depth 1:", max_at_d(T,1))
    print("Find Depth of 13:", FindDepth(T,13))
    PrintAtDepth(T,1)
    print()
    print("Number of leaves: ", NumLeafs(T))
    print("Number of full nodes: ", FullNodes(T))
    PrintDescending(T)
    print()
    print("Items in the same node as 3:", end = ' ')
    PrintItemsInNode(T,1)
    print("Number of items at depth 2", count_items(T,2))
    
    
   