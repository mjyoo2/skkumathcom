# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 11:27:08 2018

@author: mjyoo
"""

# 서로소인지 판단하기

N=input("두 자수를 입력해 주세요:")
K=[int(x) for x in N.split()] #N.split()이란 리스트 안의 x를 int형으로 바꿔서 K라는 리스트에 넣어주기
if K[0]==1 or K[1]==1:
    print("서로소 입니다")
else:
    for i in range (2,K[0]+1): # K 리스트 안의 숫자 하나를 잡아서 i를 그 숫자 까지 반복 (2부터 시작)
        if K[0]%i==0 and K[1]%i==0: # 만약 두 수가 하나의 i에 대해 나누어 떨어지면 서로소가 아니다.
            print("서로소가 아닙니다")
            break
        if i==K[0]:  # i 가 K[0]가 될때까지 break 나지 않으면, 서로소이다.
            print("서로소 입니다")
    
T=int(input("원하는 자연수를 입력해 주세요:"))
relative_prime=0 #서로소
for i in range(1,T):
    for j in range(2,T+1):
        if T%j==0 and i%j==0:
            break
        if j==T:
            relative_prime+=1

print(relative_prime)
    
