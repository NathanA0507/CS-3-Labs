# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 12:15:16 2019

@author: Natha
"""

def hanoi(n, source, spare, dest):
    if n > 0:
        hanoi(n-1, source, dest, spare)
        print('Move disk from', source, 'to', dest)
        hanoi(n-1, spare, source, dest)

hanoi(3,'A','B','C')