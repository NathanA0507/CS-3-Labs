class Node(object):
    # Constructor
    def __init__(self, data, next=None):  
        self.data = data
        self.next = next 

class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None


def buildList(plist):
    L = List()
  
  for i in range(len(plist)):
    if L.head is None:
      L.head = Node(plist[i]) 
      L.tail = Node(plist[i])
    elif L.head.next is None:
      x = Node(plist[i])
      L.head.next = x
      L.tail.next = x
      L.tail = L.tail.next
    else:
      L.tail.next = Node(plist[i])
      L.tail = L.tail.next
      
  return L
  
def split(L):
  L1 = []
  L2 = []
  iter = L.head
  while iter is not None:
    if (iter.data < L.head.data):
      L1 + [iter.data]
    else:
      L2 + [iter.data]
    iter = iter.next
  
  L1 = buildList(L1)
  L2 = buildList(L2)
  
  return L1, L2
  
  
  
TestList = [5, 10, 4, 7, 12, 30, 1, 2, 6]
List = buildList(TestList)
print(List.head.data, List.head.next.data, List.tail.data)

List1, List2 = split(List)

print(List1.head.data, List1.tail.data, List2.head.data,List2.tail.data)