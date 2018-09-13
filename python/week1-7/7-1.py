# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:33:55 2018

@author: mjyoo
"""



n=int(input("자연수를 입력해 주세요: "))
sum1=0
list_divisor=di(n)
list_divisor.sort()
for i in range(len(list_divisor)-1):
    sum1=sum1+list_divisor[i]

if sum1==n:
    print(n,"은 완전수 입니다")
else:
    print(n,"은 완전수가 아닙니다")
    
def di(n):
    list1=[]
    for i in range(1,n+1):
        if n%i==0:
            list1.append(i)
    return list1