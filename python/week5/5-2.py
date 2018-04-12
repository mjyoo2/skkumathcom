# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 13:38:57 2018

@author: mjyoo
"""

N=int(input("숫자를 입력해 주세요:"))
sum1=0
list1=[]

for i in range(1,N):
    if N%i==0:
        list1.append(i)
    
for i in range(len(list1)):
    sum1=sum1+list1[i]
    
if sum1==N:
    print("%d은(는) 완벽수입니다"%N)
else:
    print("%d은(는) 완벽수가 아닙니다"%N)