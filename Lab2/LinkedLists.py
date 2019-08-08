# -*- coding: utf-8 -*-
"""
Course: CS2302 Data Structures
Author: Nathan Aun
Assignment: Lab 2 - Linked Lists
Instructor: Dr. Fuentes
TA: Ismael Villanueva-Miranda
Date of Last Modification: 
Purpose of Program: 
"""


class Node(object):
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class List(object):
  def __init__ (self):
    self.head = None
    self.tail = None
    

def Append(L,x):
  if isEmpty(L):
    L.head = Node(x)
    L.tail = Node(x)
  else:
    L.tail.next = Node(x)
    L.tail = L.tail.next
    if L.head.next is None:
          L.head.next = L.tail    

def Prepend(L, x):
  N = Node(x,L.head)
  L.head = N
  if L.head.next is None:
    L.tail = N

def InsertAfter(L, w, x):
  foundW = False
  iter1 = L.head
  if isEmpty(L):
    print("List is empty, cannot add", x, "after", w)
  else:
    while iter1.next is not None and foundW == False:
      if iter1.data == w:
        iter1.next = Node(x,iter1.next)
        foundW = True
      else:
        iter1 = iter1.next
    if foundW == False:
      print("Did not find value", w, "in list, therefore cannot add", x,"after it")

def Remove(list1, x):
  if isEmpty(list1):
    print("list is empty, cannot remove", x)
  else:
    foundX = False
    iter1 = list1.head
    while foundX == False and iter1.next is not None:
      if iter1.next.data == x:
        iter1.next = iter.next.next 
        foundX = True
      iter1 = iter1.next
    if foundX == False:
      print("Did not find value", x, "in list, therefore cannot remove it")

def Search(list1, x):
  if isEmpty(list1):
    return None
  else:
    iter1 = list1.head
    while iter1 is not None:
      if iter1.data == x:
        print("here")
        return x
      iter1 = iter1.next
  
def Print(L):
  temp = L.head
  while temp is not None:
    print(temp.data, end = " ")
    temp = temp.next
  print()

def PrintReverse(list1):
  List1 = List()
  List1.head = list1.head.next
  if List1.head is None:
    print(list1.head.data, end = " ")
  else:
    PrintReverse(List1)
    print(list1.head.data, end = " ")

def Sort(L):
  length = 1
  temp = L.head
  while temp is not None:
    temp = temp.next
    length += 1
  length2 = length -1
  for a in range(length):
      temp = L.head
      for b in range(length2 - 1):
          if temp.data > temp.next.data:
              temp.data, temp.next.data = temp.next.data, temp.data
          temp = temp.next
      length2 -= 1
    

def isEmpty(L):
  if L.head is None:
    return True
  return False

#untested
def GetLength(L):
    iterA = L.head
    size = 0
    while iterA.next is not None:
        size += 1
        iterA = iterA.next
    return size

def Copy(L):
  if isEmpty(L):
      return None
  L2 = List()
  iterA = L.head
  while iterA is not None:
      Append(L2, iterA.data)
      iterA = iterA.next
  return L2

def ItemAt(L, n):
    iterA = L.head
    for i in range(n):
        if iterA is None:
            return None
        iterA = iterA.next
    return iterA.data

def Pop(L, i = 0):
    if i == 0:
        L.head = L.head.next
    else:
        iterA = L.head
        for k in range(i - 1):
            iterA = iterA.next
        iterA.next = iterA.next.next

def Count(L, x):
    numOccur = 0
    iterA = L.head
    while iterA is not None:
        if iterA.data == x:
            numOccur += 1
        iterA = iterA.next
    return numOccur

def Index(L, x):
    iterA = L.head
    index = 0
    while iterA is not None:
        if iterA.data == x:
            return index
        iterA = iterA.next
        index += 1
    return -1

def Clear(L):
    L.head = None
    L.tail = None
    
def Sublist(L, start = 0, end = -1):
    L2 = List()
    iterA = L.head
    if end == -1:
        end = GetLength(L)
    i = 0
    while iterA is not None and i != start:
        iterA = iterA.next
        i += 1
    while iterA is not None and i != end:
        Append(L2, iterA.data)
        iterA = iterA.next
        i += 1
    return L2
    
def Reverse(L):
    iterA = L.head
    tempList = []
    while iterA is not None:
        tempList += [iterA.data]
        iterA = iterA.next
    
    iterA = L.head
    index = len(tempList) - 1
    
    while iterA is not None:
        iterA.data = tempList[index]
        iterA = iterA.next
        index -= 1
        
  
def test():
  L = List()
  L2 = List()
  L4 = List()
  L4.head = Node(87,Node(27))
  L4.tail = L4.head.next
  L.head = Node(99,Node(77))
  L.tail = L.head.next
  L6 = List()
  L6.head = (Node(55,Node(55,Node(55,Node(55,Node(22,Node(43,Node(55))))))))
  L6.tail = L6.head.next.next.next.next.next.next
  #Appending test cases 
  print("Appending an existing list with 99 77, with 44, expected 99 77 44")
  print("actual: ", end = ' ')
  Append(L, 44)
  Print(L)
  print()
  print("Appending an empty list with 44, expected: 44")
  print("actual: ", end = ' ' )
  Append(L2, 44)
  Print(L2)
  print()
  
  #prepending test cases 
  L3 = List()
  print("Prepending an existing list with 99 77 44, with 62, expected 62 99 77 44")
  print("actual: ", end = ' ')
  Prepend(L, 62)
  Print(L)
  print()
  print("Prepending an empty list with 42, expected: 42")
  print("actual: ", end = ' ' )
  Prepend(L3, 42)
  Print(L3)
  print()
  
  #insertAfter test cases
  print("Inserting 63 after 99 in list 62 99 77 44, expected: 62 99 63 77 44")
  print("Actual: ", end = ' ')
  InsertAfter(L, 99, 63)
  Print(L)
  print()
  print("Inserting 19 after 33 but 33 is not in the list, expected: ")
  print("Actual: ", end = ' ')
  InsertAfter(L, 33, 19)
  print()
  
  '''
  #Remove Test Cases
  print("Removing 63 in list 62 99 63 77 44, expected: 62 99 77 44")
  print("Actual: ", end = ' ')
  Remove(L, 63)
  Print(L)
  print("Removing 102 in list 62 99 77 44, Should notify the user this can't be done")
  print("Actual: ", end = ' ')
  Remove(L, 102)'''
  
  #Search Test Cases
  print("Searching for 27 in list 87 27, should return 27")
  print("Actual: ", end = ' ')
  print(Search(L4, 27))
  print()
  print("Searching for 105 in list 87 27, should notify user that this num is not in the list")
  print("Actual: ", end = ' ')
  print(Search(L4, 105))
  print()
  
  #PrintReverse
  print("Printing list 87 27 in reverse, expecting 27 87")
  print("Actual: ", end = ' ')
  PrintReverse(L4)
  print()
  
  #Sort
  print("Sorting the list 62 99 77 44, expecting 44 62 77 99")
  print("Actual: ", end = ' ')
  Sort(L)
  Print(L)
  print()
  
  #isEmpty
  print("Given the list 87 27, return False")
  print("actual: ", isEmpty(L4))
  L5 = List()
  print("Given an empty list, return True")
  print("actual: ", isEmpty(L5))
  print()
  
  #GetLength
  print("Given the list 87 27, return 2")
  print("Actual: ", GetLength(L4))
  print()
  
  #Copy
  print("Copying the list 87 27 as a new list, expecting 87 27")
  print("Actual: ", end = ' ')
  L5 = Copy(L4)  
  Print(L5)
  print()
  
  #ItemAt
  print("finding the item at index 0 in a list 87 27, should return 87")
  print("Actual: ", end = ' ')
  print(ItemAt(L5,0))
  print("finding the item at index 3 in a list 87 27, should return None")
  print("Actual: ", end = ' ')
  print(ItemAt(L5,3))
  print()
  #Pop
  Print(L4)
  print("poping the first value from the above list, should only be 27 left")
  Pop(L4)
  Print(L4)
  print()
  #count
  print("Finding the amount of times 55 appears in this list")
  Print(L6)
  print("expecting 5")
  print("Actual", Count(L6,55))
  
  #Index
  print("Finding the index of 27, expecting 1")
  print("Actual: ", Index(L5, 27))
  print("Finding the index of 28, not in list so will be -1")
  print("Actual: ", Index(L5, 28))
  print()
  
  #Clear
  print("Clearing list with 87 27, should have nothing in it")
  Clear(L5)
  print("Actual: ")
  Print(L5)
  print("is L5 empty? ", isEmpty(L5))
  print()
  
  #sublist
  print("Creating a sublist of 44 62 63 77 99, from index 1-3, expecting 62 63")
  print("Actual: ", end = " ")
  L6 = Sublist(L, 1, 3)
  Print(L6)
  print()
  
  #Reverse
  print("Reversing a list with 62 63, expecting 63 62")
  print("Actual: ", end = ' ')
  Reverse(L6)
  Print(L6)
  print()
  
  
  '''
  InsertAfter(L, 77, 27)
  InsertAfter(L, 24, 27)
  InsertAfter(L2, 25, 38)
  Remove(L2, 27)
  print(Search(L,77))
  print(Search(L,80))
  Print(L)
  PrintReverse(L)
  print()
  Sort(L)
  Print(L)
  L2 = Copy(L)
  Print(L2)
  print(ItemAt(L2,3))
  Append(L2, 55)
  Append(L2, 65)
  Print(L2)
  Pop(L2)
  Print(L2)
  Pop(L2, 2)
  Print(L2)
  print(Count(L2, 77))
  Append(L2, 77)
  Append(L2, 77)
  Prepend(L2, 77)
  print(Count(L2, 77))
  Print(L2)
  print(Index(L2, 55))
  L3 = Sublist(L2, 1, 5)
  Print(L3)
  Reverse(L3)
  Print(L3)
'''
  
test()
  
  
  
  
  