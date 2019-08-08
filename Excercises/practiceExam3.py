import numpy as np

def build_dsf(k,n):
    S = np.zeros(n,dtype=int)
    S[0] = -1
    S[k] = -1
    for i in range(k+1,n):
        S[i] = k
    return S

def left_handed_and_compressed(S):
    for i in range(len(S)):
        if S[i] >= 0:
            if S[i] > i or S[S[i]] != -1:
                return False
    return True

def numSets(S):
    count = 0
    for i in S:
        if i == -1:
            count+=1
    return count

def numSetsBetter(S):
    return np.sum(S<0)
    
def isSingleton(S, i):
    if S[i] > -1:
        return False
    if i in S:
        return False
    return True

def otherIsSingleton(S,i):
    return i not in S and S[i] < 0

S = build_dsf(4,7)
S[1] = -1

print(isSingleton(S,3))
