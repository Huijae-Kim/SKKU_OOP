import random
import copy

# to make data
dim3 = []
for k in range(4):
  dim2 = []
  for j in range(4):
    dim1 = []
    for i in range(4):
      #dim1 = dim1 +[i]
      dim1.append(random.randint(1,9)) # append "1<=num<=9" element to dim1
    dim2.append(dim1)
  dim3.append(dim2)

# function of sort in dim-1
def my_sort1(data): # sort dim-1 list
  mydata=copy.deepcopy(data) # safe way to save original data
  for i in range(len(mydata)):
    for j in range(i,len(mydata)):
      if mydata[i] > mydata[j]:
        tmp = mydata[i]
        mydata[i]=mydata[j]
        mydata[j]=tmp
  return mydata

def comp2(left, right): # compare two list
  if left[0] > right[0]:
    return 0
  elif left[0] == right[0]:
    if left[1] > right[1]:
      return 0
    elif left[1] == right[1]:
      if left[2] > right[2]:
        return 0
      elif left[2] == right[2]:
        if left[3] > right[3]:
          return 0
        else:
          return 1
      else:
        return 1
    else:
      return 1
  else:
    return 1
  
def my_comp2(left, right): # compare two list
  return


# function of sort in dim-2
def my_sort2(data): # sort dim-2 list
  mydata=copy.deepcopy(data)
  for i in range(len(mydata)): # mydata is dim-2, len(mydata):# of row
    for j in range(i,len(mydata)):  
      if comp2(mydata[i],mydata[j])==0:
        tmp = mydata[i]
        mydata[i]=mydata[j]
        mydata[j]=tmp
  return mydata

def my_variance(data):
  summ = 0
  for i in range(len(data)):
    for j in range(len(data[i])): # len(data[i]): # of column
      summ = summ + data[i][j]  
  avgg = summ / (len(data)**2)
  de = 0
  for i in range(len(data)):
    for i in range(len(data[i])):
      de = de + (data[i][j]-avgg)**2
  var = de / (len(data)**2)
  return var

def my_sort3(data): # sort dim-3 list
  mydata=copy.deepcopy(data)
  var_list = []
  for i in range(len(mydata)):
    var_list.append(my_variance(mydata[i]))
  # var_list = [vari(data[i] for i in range(len(data))] # list comprehension
  print "var_list=", var_list
  for i in range(len(var_list)): # mydata is dim-2, len(mydata):# of row
    for j in range(i,len(var_list)):
      if var_list[i] > var_list[j]:
        print var_list[i], var_list[j]
        tmpv = var_list[i]
        var_list[i]=var_list[j]
        var_list[j]=tmpv

        tmp = mydata[i]
        mydata[i]=mydata[j]
        mydata[j]=tmp

        print var_list
        print mydata
  return mydata

my_sort3(dim3)

# function of average
def my_avg(data):
  summ = 0
  cnt = 0
  for i in data:
    cnt += 1 # cnt = cnt + 1
    summ = summ + i
  return summ / cnt




r=[]
for i in range(10):
  r.append(random.randint(0,9))

print r

# original bubble sort
for i in range(len(r)-1):
  for j in range(0,len(r)-1-i):
    if r[j]>r[j+1]:
      r[j],r[j+1]=r[j+1],r[j]

print r

r=[]
for i in range(5):
  r.append(random.randint(0,9))

print r

# heejae's style bubble sort
for i in range(len(r)-1):
  for j in range(i+1,len(r)):
    print i, j
    if r[i]>r[j]:
      r[i],r[j]=r[j],r[i]
      print r
    print "================="
      
print r
