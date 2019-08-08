import math
import numpy as np
import random

f = '(n+10)*(n+10)'
g = 'n*n + 20*n + 100'


def sameFunction(f,g, numTries = 1000, tolerance = 0.00001):
    for i in range(numTries):
        n = random.random()
        y1 = eval(f)
        y2 = eval(g)
        if np.abs(y1-y2) < tolerance:
            return True
        return False
print(sameFunction(f,g))
g = 'n-3'
print(sameFunction(f,g))