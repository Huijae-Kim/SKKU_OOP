import random

def comp2(left, right): # compare two list
  if left[0] > right[0]:
    return "left is big"
  elif left[0] == right[0]:
    if left[1] > right[1]:
      return "left is big"
    elif left[1] == right[1]:
      if left[2] > right[2]:
        return "left is big"
      elif left[2] == right[2]:
        if left[3] > right[3]:
          return "left is big"
        else:
          return "left is small"
      else:
        return "left is small"
    else:
      return "left is small"
  else:
    return "left is small"

# how to make the function above more clearly
def my_comp2(left, right): # compare two list
  while len(left)==len(right):
    if left==right:
      return "both are same"
    for i in range(len(left)):
      if left[i] > right[i]:
        return "left is big"
      elif left[i] == right[i]:
        i+=1
        continue
      else:
        return "left is small"
        
data1 = [1,2,3,4]
data2 = [1,2,3,5]
#print comp2(data1,data2)
#print my_comp2(data1,data2)

# swap function
def my_swap(data,i,j):
  data[i],data[j]=data[j],data[i]

# buuble sort function
def my_bubble_sort(data):
  mydata = data[:]
  for i in range(len(mydata)-1):
    for j in range(0,len(mydata)-i-1):
      if mydata[j] > mydata[j+1]:
        my_swap(mydata,j,j+1)
  return data

data3 = []
for i in range(9):
  data3.append(random.randint(0,100))

#print data3
#print my_bubble_sort(data3)

# min function
def my_min(data):
  min_value = data[0]
  for i in range(1,len(data)):
    if min_value > data[i]:
      min_value=data[i]
  return min_value
  
# index function
def my_index(data,value):
  for i in range(len(data)):
    if data[i]==value:
      break
  return i

# slection sort function
def my_selection_sort(data):
  mydata = data[:]
  result = []
  while len(result)<len(data):
    min = my_min(mydata)
    print min
    result.append(min)
    print "result=", result
    print "min index=", my_index(mydata,min)
    mydata.pop(my_index(mydata,min))
    print "mydata=", mydata
    print "==================="
  return result

print data3
print "=================="
my_selection_sort(data3)
    
    
    
    

