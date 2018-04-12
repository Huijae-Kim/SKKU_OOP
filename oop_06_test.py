#-*- coding: utf-8 -*-
"""
<<문제>>
(n,n)의 2차원 리스트가 주어졌을 때
1차원에서는 숫자 크기의 오름차순으로 정렬,
2차원에서는 숫자 크기의 오름차순으로 정렬하되 만일 숫자가 동일하다면 다음 인덱스의 크기를 비교하여 정렬을 하여 리스트를 반환하는 함수를 작성하라
"""

import random

data2 = []
for i in range(5):
    data1 = []
    for j in range(5):
        data1.append(random.randint(0, 3))
    data2.append(data1)

# print data2


def my_sort1(data1):
    mydata = data1[:]
    for i in range(len(mydata)-1):
        for j in range(0,len(mydata)-1-i):
            if mydata[j] > mydata[j+1]:
                mydata[j],mydata[j+1]=mydata[j+1],mydata[j]
    return mydata

# print my_sort1([4,1,3,56,4,5,2,3,5,6,7,3234,32,46,0])


def my_comp2(left,right):
    if left==right:
        return 0 # left=right
    i = 0
    for i in range(len(left)):
        if left[i]>right[i]:
            return -1 # left>right
        elif left[i]==right[i]:
            i += 1
            continue
        else:
            return 1 # left<right

data11 = []
data12 = []
for i in range(5):
    data11.append(random.randint(0,5))
for i in range(5):
    data12.append(random.randint(0,5))

# print my_sort1(data11)
# print my_sort1(data12)
# print my_comp2(my_sort1(data11),my_sort1(data12))


def my_sort2(data2):
    mydata=data2[:]
    for i in range(len(mydata)):
        mydata[i]=my_sort1(mydata[i])
    # print mydata
    for i in range(len(mydata)-1):
        for j in range(0,len(mydata)-1-i):
            if my_comp2(my_sort1(mydata[j]), my_sort1(mydata[j+1]))==-1:
                mydata[j],mydata[j+1]=mydata[j+1],mydata[j]
    return mydata

# print my_sort2(data2)
