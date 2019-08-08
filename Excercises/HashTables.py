class HashTable(object):
    #builds a hash table of size 'size'
    #bucket is a list of (intitially empty) lists
    #constructor
    def __init__(self,size):
        self.bucket = [[] for i in range(size)]
    
def h(H,k):
    return k % len(H.bucket)

def Insert(H, k):
    Hval = h(H,k)
    try:
        H.bucket[Hval].index(k)
    except:
        H.bucket[Hval].insert(0,k) 
    
def Find(H,k):
    Hval = h(H,k)
    try:
        H.bucket[Hval].index(k)
        Delete(H,k)
        Insert(H,k)
        i = 0
    except:
        i = -1
    return H.bucket[Hval], i

def Delete(H, k):
    bucket, index = Find(H, k)
    if index < 0:
        print("Cannot delete item from list, does not exist")
    else:
        bucket.remove(k)
        
def LoadFactor(H):
    size = 0
    for i in H.bucket:
        size += len(i)
    return size / len(H.bucket)

def WorstAccess(H):
    size = 0
    for i in H.bucket:
        size = max(size, len(i))
    return size
    
def Verify(H):
    for i in range(len(H.bucket)):
        for k in range(len(H.bucket[i])):
            if H.bucket[i][k] % len(H.bucket) != i:
                return False
    return True

def total_keys(H):
    total = 0
    for i in H.bucket:
        total += len(i)
    return total


if __name__ == "__main__":
    H = HashTable(7)
    
    L = [12, 3, 21, 14, 11, 8, 9, 7, 6, 1, 22, 19]
    
    H2 = HashTable(7)
    for i in L:
        Insert(H2,i)
    
    for i in range(100):
        Insert(H,i)
    
    TempList, index = Find(H, 21)
    print(TempList[index])
    
    TempList2, index = Find(H2, 21)
    
    print(TempList2, index, TempList2[index])
    
   # Delete(H2, 21)
    Insert(H2, 21)
    
    TempList2, index = Find(H2, 7)
    
    print(TempList2, index, TempList2[index])
    
  #  Delete(H2, 21)
    
    print("Load factor", LoadFactor(H2))
    print("worst access is ", WorstAccess(H2))
    
    print("Verify ", Verify(H2))
    print(H2.bucket)
    print("total keys", total_keys(H2))
    
    
    
    
    