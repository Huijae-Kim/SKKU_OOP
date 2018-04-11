#-*- coding: utf-8 -*-
"""
<<문제>>
4,4,4 3차원 list
1차원 : 행렬 안 숫자를 오름차순으로 정리
2차원 : 첫번째 숫자끼리 비교하여 오름차순으로 정리하되, 같은 숫자일 경우 다음 숫자로 넘어가서 비교한다.
3차원 : 행렬 간의 분산을 비교하여 정리
"""

print "Sangyeon is babo."

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
#	print mean
	sum_diff2=0
	for i in range(0,4):
		for j in range(0,4):
#			print "{},{} : {}".format(i,j,(input[i][j]-mean)**2)
			sum_diff2 = sum_diff2 + (input[i][j]-mean)**2
#			print "total : {}\n".format(sum_diff2)
	var = sum_diff2 / 16.
#	print var
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
#				 [[1,2,3,4],[4,5,6,7],[7,8,9,10],[10,11,12,13]],
#				 [[1,2,3,4],[3,4,5,6],[5,6,7,8],[7,8,9,10]],
#				 [[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]]
#print increase3(data4)

def main(input):
	# dim-1
	for i in range(0,4):
		for j in range(0,4):
			input[i][j]=increase1(input[i][j])
#			print input[i][j]
#	print "\n"
	# dim-2
	for k in range(0,4):
		input[k]=increase2(input[k])
#		print input[k]
#	print "\n"
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

