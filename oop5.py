# function to get ordinal number
def get_ordinal_number(num):
	if num == 1 or (int(str(num)[-2:]) % 10 == 1 and int(str(num)[-2:]) // 10 >= 2):
		return "{}st".format(num)
	elif num == 2 or (int(str(num)[-2:]) % 10 == 2 and int(str(num)[-2:]) // 10 >= 2):
		return "{}nd".format(num)
	elif num == 3 or (int(str(num)[-2:]) % 10 == 3 and int(str(num)[-2:]) // 10 >= 2):
		return "{}rd".format(num)
	else:
		return "{}th".format(num)

#for i in range(1,40):
#	print "{} = {} / ".format(i,get_ordinal_number(i)),
	
# swap change the location
#A=[1,2,3,4]
#A[0],A[3]=A[3],A[0]
#print A

# [hj] function of reverse
def reverse1(data):
	length = len(data)
	result = []
	for i in range(0,length):
		result += [data[-i-1]]
	return result

# test
#print "[hj] reverse function"
#print "input : {} - ouput : {}".format(range(1,6), reverse1(range(1,6)))

# [prof] function of reverse
def reverse2(data):
	result = []
	while len(data) >= 1:
		result = [data.pop(0)] + result
		# pop() : take the value & erase the value in the list
	return result

# test 
#print "[prof] reverse function"
#print "input : {} - ouput : {}".format(range(1,6), reverse2(range(1,6)))

# [prof] range function w/ one argv
def range1(num):
	result = []
	i=0
	while i<num:
		result += [i]
		i = i + 1
	return result

# test
#print "[prof] range function w/ one argv"
#print "input : 10 - output : {}".format(range1(10))

# [hj] range function w/ two argv
def range2(num1,num2):
	result = []
	i=num1
	while i<num2:
		result += [i]
		i += 1
	return result

# test
#print "[hj] range function w/ two argv"
#print "input : (1,6) - output : {}".format(range2(1,6))

# [hj] moving average function
def moving_average1(input, w_size=3):
	output=[]
	for i in range(0,(len(input)-w_size+1)):
		average = float(sum(input[i:(i+w_size)]))/float(w_size)
		output += [average]
	return output

# [prof] moving average function : test for last week
def moving_average2(data,window_size=2): 
	#default of window size is 2, when you want to have default value, then argument should be written back.
	
	ma_data=[]
	reversed_data=list(reversed(data))
	#reversed(data) is object... so sholud put in list()

	for i in range(len(reversed_data)):
		
		#unless loop break. break condition sholud be written on top	
		if i == len(reversed_data)-window_size+1: 
			break

#		# (1) show ordinal number
#		if i+1==1 or ((i+1)%10==1 and (i+1)//10>=2):
#			print "\nwindow calculation: {}st".format(i+1)
#		elif i+1==2 or ((i+1)%10==2 and (i+1)//10>=2):
#			print "\nwindow calculation: {}nd".format(i+1)
#		elif i+1==3 or ((i+1)%10==3 and (i+1)//10>=2):
#			print "\nwindow calculation: {}rd".format(i+1)
#		else:
#			print "\nwindow calculation: {}th".format(i+1)
		
		# (2) show #000 
		# print "\nwindow calculation: #{:03}".format(i+1)
		#total 3numbers, front of the number filled by 0

		sum=0

		for j in range(window_size):
#			if j==0:
#				print"( {}".format(reversed_data[i+j]),
#			elif j == window_size -1:
#				print "+ {} ) / {}. -->".format(reversed_data[i+j], window_size),
#			else:
#				print "+ {}".format(reversed_data[i+j]), 
#				# if you write , print in one line.
			sum=sum+reversed_data[i+j]

		result = sum / float(window_size)
#		print result
		ma_data = ma_data + [result]

	return list(reversed(ma_data))

# test
#print "[prof] moving average function"
#a = range(1,11)
#print "input : 1~10, window size 4 - output : {}".format(moving_average2(a,4))




