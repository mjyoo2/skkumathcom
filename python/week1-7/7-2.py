# -*- coding: utf-8 -*-
"""
Created on Wed May  2 16:40:03 2018

@author: mjyoo
"""

def gugudan(n):
    for i in range(1,10):
        print("%d*%d=%2d"%(n,i,n*i))
        
def gugudan2(n):
    for i in range(len(n)):
        for j in range(1,10):
            print("%d*%d=%2d"%(n[i],j,n[i]*j))
