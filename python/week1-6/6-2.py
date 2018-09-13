# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 12:28:21 2018

@author: mjyoo
"""

list1=[4,6,2,8,19,3,6,8]

for i in range(1,len(list1)):
    num=i
    for j in range(i-1,-1,-1):
        if list1[i]<list1[j]:
            num=j
        else:
            break
    K=list1[i]
    for k in range(i,num,-1):
        list1[k]=list1[k-1]
    list1[num]=K

print(list1)
    
    