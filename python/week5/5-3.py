# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 13:10:44 2018

@author: mjyoo
"""
n=int(input("숫자를 입력해 주세요:")) #어떤 수가 한수인지 확인해보자
if n<=99: #n이 두자리 자연수일때는 항상 한수이다.
    print("한수 입니다")
else: #세자리 자연수일 때는 각 자리수가 등차수열인지를 확인해야 한다
    a=n//100            #첫번째 자릿수 a 구하기
    b=(n-100*a)//10     #두번째 자릿수 b 구하기
    c=(n-100*a-10*b)    #세번째 자릿수 c 구하기
    if (a-b)==(b-c):    #등차수열인지 확인하기
        print("한수 입니다.")
    else:
        print("한수가 아닙니다")




n=int(input('숫자를 입력해 주세요: '))
han=0  #n보다 작은 한수의 개수 n
for i in range(1,n+1):  #n보다 작은 자연수에 대해서 한수인지 확인하
    if i<=99:   #위의 한수인지 판단하는 코드와 같다
        han+=1
    else:
        a=i//100
        b=(i-100*a)//10
        c=(i-100*a-10*b)
        if (a-b)==(b-c):
            han+=1
print(han)

