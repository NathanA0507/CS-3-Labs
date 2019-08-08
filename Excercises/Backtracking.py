# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 11:44:35 2019

@author: Natha
"""

def subsetsum(S,goal):
    if goal == 0:
        return True
    if goal < 0 or len(S) == 0 or sum(S) < goal:
        return False
    return subsetsum(S[1:],goal-S[0]) or subsetsum(S[1:],goal)

