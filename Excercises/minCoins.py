import numpy as np

def min_coins(c,den):
    C = np.zeros(c+1,dtype = int) + 100000
    C[0] = 0
    for i in range(1,len(C)):
        for d in den:
            if i >= d and C[i] > C[i-d]+1:
                C[i] = C[i-d] + 1
    return C[-1]

def min_coins2(totalVal,coinVal):
    coins = np.zeros(totalVal+1,dtype=int)+10000
    coins[0] = 0
    for c in coinVal:
        for d in range(c, totalVal+1):
            if coins[d-c] +1 < coins[d]:
                coins[d] = coins[d-c] + 1
    return coins[-1]
            

print(min_coins(10,[1,3,5]))
print(min_coins2(10,[1,3,5]))