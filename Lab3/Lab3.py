import numpy as np
import random
'''
Course: CS2302 Data Structures
Author: Nathan Aun
Assignment: Lab 3 - Decision Trees
Instructor: Dr. Fuentes
TA: Ismael Villanueva-Miranda
Date of Last Modification: 7/8/2019 
Purpose of Program: To use decision trees to predict if a given
 wave is a gamma ray based on 1/10 attributes, chosen at random
'''
class decisionTreeNode(object):
    # Constructor
    def __init__(self, att, thr, left, right):  
        self.attribute = att
        self.threshold = thr
        # left and right are either bynary classifications, or references to 
        # decision tree nodes
        self.left = left     
        self.right = right    

def entropy(l,m=[]):
    ent = 0
    for p in [l,m]:
        if len(p)>0:
            pp = sum(p)/len(p)
            pn = 1 -pp
            if pp<1 and pp>0:
                ent -= len(p)*(pp*np.log2(pp)+pn*np.log2(pn))
    ent = ent/(len(l)+len(m))
    return ent

def classify(DT, atts):
    if atts[DT.attribute] < DT.threshold:
        if DT.left in [0,1]:
            return DT.left
        else:
            return classify(DT.left, atts)
    else:
        if DT.right in [0,1]: 
            return DT.right
        else:
            return classify(DT.right, atts)

#Num nodes will take a decision tree node and return the number of nodes in that tree
def NumNodes(DT):
    if DT == 0 or DT == 1:
        return 1
    temp = 0
    temp += NumNodes(DT.left) + 1 + NumNodes(DT.right)
    return temp

#Height will take a decision tree node and return the height of that tree
def Height(DT):
    if DT == 0 or DT == 1:
        return 1
    height = max(Height(DT.left) + 1,Height(DT.right) + 1)
    return height

#AttributeSplitBy will take a Decision Tree and an array of size 10, and will increment 
#The index of the value used to split in that place
def AttributeSplitBy(DT, arr):
    if DT == 0 or DT == 1:
        return arr
    arr[DT.attribute] += 1
    arr = AttributeSplitBy(DT.left, arr)
    arr = AttributeSplitBy(DT.right, arr)
    return arr
  
#Average will take an array of 5 classified DT data, and will set the value to whatever the 
#majority is. Will only work with 5 classified DT's but can be tweaked to work for other values
def Average(arr):
    for i in range(len(arr)):
        if arr[i] >= 3:
            arr[i] = 1
        else:
            arr[i] = 0
    return arr

def buildDT(attributes, target, n_splits, goal_acc, min_size):
    # Builds a one-node decision tree to classify data
    # It tries n_splits random splits and keeps the one that results in the lowest entropy
    if n_splits < 10:
        n_splits == 10
    print('examples:',len(target), ' default accuracy',max([np.mean(target),1-np.mean(target)]))
    print('Trying random splits')
    best_ent = 1
    min_att_val = np.min(attributes,axis=0)
    for i in range(n_splits):
        while True:
            a = random.randrange(attributes.shape[1])
            #print("a", a)
            ex = random.randrange(attributes.shape[0])
            #print("Ex,", ex)
            thr = attributes[ex,a]
            #print("Thr ", thr)
            if thr>min_att_val[a]: # making sure we don't have an empty splits
                break
        less = attributes[:,a] < thr
        #print("less", len(less), less)
        more = ~ less
        #print("more", len(more), more)
        #print("Target: ", len(target), target)
        tgt_less = target[less]
        #print("tgt less",len(tgt_less), tgt_less)
        tgt_more = target[more]
        #print("tgt more", len(tgt_more), tgt_more)
        if len(less)==0 or len(more) ==0:
            ent = 1
        else:
            ent = entropy(tgt_less,tgt_more)
        #print(i,a,thr,ent) # Used for debugging
        if ent < best_ent:
            best_ent, best_a, best_thr =  ent, a, thr
            left_child = int(np.mean(tgt_less)+.5)
            right_child = int(np.mean(tgt_more)+.5)
            left_best_split = less
            right_best_split = more
            #print(a,thr,ent) # Used for debugging
    print('Best split:',best_a,best_thr,best_ent)
    ml = np.mean(target[left_best_split])
    left_acc = max([ml,1-ml])
    left_size = np.sum(left_best_split)
    mm = np.mean(target[right_best_split])
    right_acc = max([mm,1-mm])
    right_size = np.sum(right_best_split)
    print('Accuracies:',left_acc,right_acc)
    print('Sizes:',left_size,right_size)
    
    # if left_acc is less than goal accuracy and left_size is greater than min_size
    # build left decision subtree recursively
    # does the same for the right side
    if left_acc < goal_acc and left_size > min_size:
        left_child = buildDT(attributes[left_best_split], target[left_best_split], n_splits, goal_acc, min_size)
    if right_acc < goal_acc and right_size > min_size:
        right_child = buildDT(attributes[right_best_split], target[right_best_split], n_splits, goal_acc, min_size)
    return decisionTreeNode(best_a, best_thr, left_child, right_child)
    
attributes = []
target = []
infile = open("magic04.txt","r")
for line in infile:
    target.append(int(line[-2:-1] =='g'))
    attributes.append(np.fromstring(line[:-2], dtype=float,sep=','))
infile.close()
attributes = np.array(attributes) 
target = np.array(target) 


#Split data into training and testing
ind = np.random.permutation(len(target))
split_ind = int(len(target)*0.8)
train_data = attributes[ind[:split_ind]]
test_data = attributes[ind[split_ind:]]
train_target = target[ind[:split_ind]]
test_target = target[ind[split_ind:]]

#Constructing multiple decision trees to average them together to get more accurate data
#Try around 51?
'''
dt1 = buildDT(train_data, train_target, 100, 0.95, 25) #1000 200
dt2 = buildDT(train_data, train_target, 1000, 0.95, 200)
dt3 = buildDT(train_data, train_target, 1000, 0.95, 250)
dt4 = buildDT(train_data, train_target, 100, 0.95, 5)
dt5 = buildDT(train_data, train_target, 100, 0.95, 20)
'''
dt = []
for i in range(51):
    dt.append(buildDT(train_data, train_target, 100, .95, 25))

train_pred = np.zeros(train_target.shape, dtype=int)
#Classifying each tree and putting it in an array
for i in range(len(train_pred)):
    for j in range(len(dt)):
        train_pred[i] += classify(dt[j], train_data[i])
    #print("Train prediction predivide:", train_pred[i], end = ' ')
    train_pred[i] = round(train_pred[i] / len(dt))
    #print("postdivide 2:", train_pred[i])
#train_pred = Average(train_pred) #Average will make it so there are only 1's and 0s in the array
train_acc = np.sum(train_pred==train_target)/len(train_pred)
print('train accuracy:', train_acc)

test_pred = np.zeros(test_target.shape, dtype=int)
#Same reason for train_pred, classifying each tree and putting it in an array
for i in range(len(test_pred)):
    for j in range(len(dt)):
        test_pred[i] += classify(dt[j], test_data[i])

    #print("test prediction", test_pred[i])
    test_pred[i] = round(test_pred[i] / len(dt))
#test_pred = Average(test_pred) #Averaging each element of the arr to see if it's majority 1's or 0's
test_acc = np.sum(test_pred==test_target)/len(test_pred)
print('test accuracy:', test_acc)

arr = np.zeros(10, dtype=int)
#Printing data for each tree
print('Number of nodes for dt[0]', NumNodes(dt[0]))
print('Height of dt[0]', Height(dt[0]))
print('times each attribute was used to split dt[0]', AttributeSplitBy(dt[0],arr))
