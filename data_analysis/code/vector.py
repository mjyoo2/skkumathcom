# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 11:19:58 2018

@author: mjyoo
"""

import math

def vector_add(v,w): #벡터의 합
    return [v_i+w_i
            for v_i,w_i in zip(v,w)]

def vector_subtract(v,w): #벡터의 차
    return [v_i-w_i
            for v_i,w_i in zip(v,w)]

def vector_sum(vectors): #벡터들의 합
    result=vectors[0]
    for vector in vectors[1:]:
        result=vector_add(result,vector)
    return result

def scalar_multiply(c,v): #벡터의 스칼라곱
    return[c*v_i for v_i in v]

def vector_mean(vectors): #벡터의 평균값(각 성분의 평균값)
    n=len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))

def dot(v,w): #벡터의 내적
    return sum(v_i*w_i for v_i,w_i in zip(v,w))

def magitude(v): #벡터의 크기
    return math.sqrt(dot(v,v))

def distance(v,w):
    return magitude(vector_subtract(v,w))
