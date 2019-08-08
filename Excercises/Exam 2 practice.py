# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:20:16 2019

@author: Natha
"""

def sum_items(T,d):
    if d == 0:
        return T.item
    tempSum = 0
    if T.left is not None:
        tempSum += sum_items(T.left, d-1)
    if T.right is not None:
        tempSum += sum_items(T.right, d-1)
    return tempSum

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


def leftChild(i):
    return i*2 + 1
def rightChild(i):
    return i*2 + 2

def findParent(i):
    return (i-1) // 2
def checkHeap(H):
    for i in range(1,len(H)):
        if H[i] > H[findParent(i)]:
            return False
    return True

#total keys in a hash table that chains
def total_keys(H):
    total = 0
    for i in H.bucket:
        total += len(i)
    return total

#total keys in a hash table with linear probing
def total_keys2(H):
    total = 0
    for i in H.item:
        if i >=0:
            total += 1
    return total







