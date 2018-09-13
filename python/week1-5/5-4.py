# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 11:13:27 2018

@author: mjyoo
"""
list1=[]
list2=[]
list3=[]
list_single=[]
list_double=[]
list_bull=[]
list_triple=[]

for i in range(1,21):
    list_single.append(i)
    list_double.append(2*i)
    list_triple.append(3*i)    

list_bull.append(50)

for i in range(1,21):
    if list1.count(i)==0:
        list1.append(i)
    if list1.count(i*2)==0:
        list1.append(i*2)
    if list1.count(i*3)==0:    
        list1.append(i*3)

list1.append(50)
        
for i in range (len(list1)):
    for j in range(len(list1)):
        if list2.count(list1[i]+list1[j])==0:
            list2.append(list1[i]+list1[j])

for i in range(len(list2)):
    for j in range(len(list1)):
        if list3.count(list1[j]+list2[i])==0:
            list3.append(list1[j]+list2[i])
    
list1.append(50)
list1.sort()
list2.sort()
list3.sort()

def num_check(x):
    if x in list1:
        return 1
    elif x in list2:
        return 2
    elif x in list3:
        return 3
    else:
        return 0
    
def print_check(N):
    if N in list_single:
        print("single %d"%N)
    elif N in list_double:
        print("double %d"%(N/2))
    elif N in list_bull:
        print("Bull")
    elif N in list_triple:
        print("triple %d"%(N/3))

N=int(input("남은 점수를 입력해 주세요: "))

if N<=0:
    print("점수를 잘 못 입력하셧습니다. ")
elif num_check(N)==0:
    print("세개의 다트로 끝낼 수 없습니다.")
elif num_check(N)==1:
    print_check(N)
elif num_check(N)==2:
    for i in range(0,len(list1)):
        if num_check(N-list1[i])==1:
            print_check(N-list1[i])
            print_check(list1[i])
            break
elif num_check(N)==3:
    for i in range(0,len(list2)):
        if num_check(N-list2[i])==2:
            for j in range(0,len(list1)):
                if num_check(N-list2[i]-list1[j])==1:
                    print_check(N-list1[j]-list2[i])
                    print_check(list1[j])
                    print_check(list2[i])
                    k=1
                    break
            if k==1:
                break
    