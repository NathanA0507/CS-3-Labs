# -*- coding: utf-8 -*-

class BST(object):
    #constructor
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right
    
def InsertBST(T, newItem):
    if T is None:
        T = BST(newItem)
    elif T.item > newItem:
        T.left = InsertBST(T.left, newItem)
    else:
        T.right = InsertBST(T.right, newItem)
    return T

def InOrder(T):
    if T is not None:
        InOrder(T.left)
        print(T.item, end = " ")
        InOrder(T.right)

def Smallest(T):
    if T.left is None:
        return T
    return Smallest(T.left)
    
def Largest(T):
    if T.right is None:
        return T
    return Largest(T.right)

def Find(T, k):
    if T is None:
        return None
    if T.item == k:
        return T
    elif T.item > k:
        return Find(T.left, k)
    elif T.item < k:
        return Find(T.right, k)
    
    
def numNodes(T):
    if T is None:
        return 0
    return 1 + numNodes(T.left) + numNodes(T.right)

def Height(T):
    if T is None:
        return -1
    temp1 = numNodes(T.left)
    temp2 = numNodes(T.right)
    return 1 + max(temp1, temp2)
    
#Excercise 2
    
def PrintLessThanK(T, k):
    if T is None:
        return
    if T.item < k:
        print(T.item, end = " ")
    PrintLessThanK(T.left, k)
    PrintLessThanK(T.right,k)
    
def printAtDepth(T,d):
    if T is not None:
        if d == 0:
            print(T.item, end = ' ')
        else:
            printAtDepth(T.left, d-1)
            printAtDepth(T.right, d-1)
            
    
def balancedTree(L, T = None):
    if len(L) == 0:
        return None
    mid = (len(L) // 2) 
    return BST(L[mid], balancedTree(L[:mid], T), balancedTree(L[mid+1:], T) )

def ShowTree(T, ind):
    if T is not None:
        ShowTree(T.right,ind+'  ')
        print(ind, T.item)
        ShowTree(T.left,ind+'  ')

def sum_items(T,d):
    if d == 0:
        return T.item
    tempSum = 0
    if T.left is not None:
        tempSum += sum_items(T.left, d-1)
    if T.right is not None:
        tempSum += sum_items(T.right, d-1)
    return tempSum        

def test():
    T = None
    A = [70, 50, 90, 130, 150, 40, 10, 30, 100]
    for a in A:
        T = InsertBST(T, a)
    
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    T2 = None
    T2 = InsertBST(T2, 10)
    
    InOrder(T)
    print()
    print(Smallest(T).item)
    print(Largest(T).item)
    
    #print(Find(T, 90))
    
    #print(numNodes(T))
    #print(Height(T))
    #print(Height(T2))
    
    #PrintLessThanK(T, 100)
    #PrintLessThanK(T2, 10)
    
    T3 = balancedTree(L)
    #print(T3.item)
    #print(T3.left.item, T3.right.item)
    #InOrder(T3)
    ShowTree(T3,' ')
    
    print(sum_items(T3, 1))
    print(sum_items(T3, 2))
    print(sum_items(T3, 5))
    
test()
