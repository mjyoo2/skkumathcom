# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 12:36:52 2018

@author: mjyoo
"""

for i in range(2,10):
    for j in range(1,10):
        print("%d * %d = %-2d"%(i,j,i*j),end=' ')
    print()