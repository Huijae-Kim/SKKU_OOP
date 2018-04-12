#-*- coding: utf-8 -*-
"""
<<문제>>
(4,4,4)의 3차원 리스트가 주어졌을 때
1차원에서는 숫자 크기의 오름차순으로 정렬,
2차원에서는 숫자 크기의 오름차순으로 정렬하되 만일 숫자가 동일하다면 다음 인덱스의 크기를 비교하여 정렬,
3차원에서는 숫자들의 분산 크기의 오름차순으로 정렬을 하여 리스트를 반환하는 함수를 작성하라
단, 파이썬 자체의 내장 정렬함수 또는 추가패키지를 활용한 정렬은 불가하다.
"""

def increase1(input):
  for i in range(0,4):
    for j in range(i+1,4):
      if input[i]>input[j]:
        input[i],input[j]=input[j],input[i]
  return input

#test
#data1 = [3,4,2,1]
#print increase1(data1)

def increase2(input):
  for i in range(0,4):
    for j in range(i+1,4):
      k=0
      while k<4:
        if input[i][k]>input[j][k]:
          input[i],input[j]=input[j],input[i]
        else:
          k=k+1 
  return input

#test
#data2 = [[2,4,5,6],[2,3,4,5],[1,2,4,5],[1,2,3,4]]
#print increase2(data2)

def get_variance(input):
  sum=0
  for i in range(0,4):
    for j in range(0,4):
      sum = sum + input[i][j]
  mean = sum / 16.
#  print mean
  sum_diff2=0
  for i in range(0,4):
    for j in range(0,4):
#      print "{},{} : {}".format(i,j,(input[i][j]-mean)**2)
      sum_diff2 = sum_diff2 + (input[i][j]-mean)**2
#      print "total : {}\n".format(sum_diff2)
  var = sum_diff2 / 16.
#  print var
  return var
  
#test
#data3 = [[0,0,0,0],[2,2,2,2],[2,2,2,2],[4,4,4,4]]
#print get_variance(data3)

def increase3(input):
  for i in range(0,4):
    for j in range(i+1,4):
      if get_variance(input[i]) > get_variance(input[j]):
        input[i],input[j]=input[j],input[i]
  return input
  
#test
#data4 = [[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
#         [[1,2,3,4],[4,5,6,7],[7,8,9,10],[10,11,12,13]],
#         [[1,2,3,4],[3,4,5,6],[5,6,7,8],[7,8,9,10]],
#         [[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]]
#print increase3(data4)

def main(input):
  # dim-1
  for i in range(0,4):
    for j in range(0,4):
      input[i][j]=increase1(input[i][j])
#      print input[i][j]
#  print "\n"
  # dim-2
  for k in range(0,4):
    input[k]=increase2(input[k])
#    print input[k]
#  print "\n"
  # dim-3
  input=increase3(input)
  return input

data = [[[4,3,2,1],
         [5,3,4,1],
         [8,9,3,2],
         [6,5,2,3]],
        [[5,4,3,2],
         [9,8,7,6],
         [13,12,11,10],
         [15,14,13,12]],
        [[6,5,4,3],
         [10,9,8,7],
         [14,13,12,11],
         [18,17,16,15]],
        [[7,6,5,4],
         [11,10,9,8],
         [15,14,13,12],
         [19,18,17,16]]]  

print main(data)

    

