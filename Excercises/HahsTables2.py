import numpy as np

class HashTable(object):
    #builds a hash table of size 'size', initializes items to -1 (which means empty)
    #Constructor
    def __init__(self, size):
        self.item = np.zeros(size,dtype=np.int)-1

def Insert(H,k):
    #Inserts k in H until H is full
    #Returns the position of k in H, or -1 if k could not be inserted
    for i in range(len(H.item)):
        pos = (k + i) % len(H.item)
        if H.item[pos] == k:
            break
        if H.item[pos] < 0:
            H.item[pos] = k
            return pos
    return -1

def Find(H,k):
    temp = -1
    #Returns the position of k in H, or -1 if k is not in the table
    for i in range(len(H.item)):
        pos = (k+i)%len(H.item)
        if H.item[pos] == k:
            if temp >= 0:
                H.item[temp] = k
                H.item[pos] = -2
                pos = temp
            return pos
        if H.item[pos] == -1:
            return -1
        if H.item[pos] == -2 and temp < 0:
            temp = pos
    return -1

def Delete(H,k):
    #Deletes k from H. It returns the position where k was, or -1, if k was not in the table
    #Sets table item where k was to -2 (which means deleted)
    f = Find(H,k)
    if f >= 0:
        H.item[f] = -2
    return f

def LoadFactor(H):
    count = 0
    for i in H.item:
        if i >= 0:
            count += 1
    return count / len(H.item)

def NumCollisions(H):
    count = 0
    for i in range(len(H.item)):
        if (H.item[i] >= 0) and (i != (H.item[i] % len(H.item))):
            count += 1
    return count

def total_keys(H):
    total = 0
    for i in H.item:
        if i >=0:
            total += 1
    return total

if __name__ == "__main__":
    H = HashTable(7)
    Insert(H,13)
    Insert(H,6)
    Insert(H,15)
    Insert(H,18)
    Delete(H,15)
    Insert(H,20)
    Insert(H,10)
    Delete(H,13)
    Insert(H,10)
    print(H.item)
    print("load factor",LoadFactor(H))
    print("number of collisons",NumCollisions(H))
    Delete(H,20)
    print(H.item)
    print(Find(H,18))
    print(H.item)
    print("total keys", total_keys(H))
    
    
    