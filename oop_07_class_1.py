# last week test

import random
import copy

n = random.randint(2,9)
m = random.randint(2,9) # available for n x m matrix form

# n x n matrix
r1 = []
for i in range(n-1):
    a = []
    for j in range(n-1):
        a.append(random.randint(0,10))
    r1.append(a)

# n x m matrix
r2 = []
for i in range(n-1):
  a = []
  for j in range(m-1):
    a.append(random.randint(0,10))
  r2.append(a)

# greater than function
def gt(a, b):
  if len(a) is not len(b):
    raise Exception
    # return False
  for i in range(len(a)):
    if a[i] == b[i]:
      continue
    elif a[i] > b[i]:
      return True
    else:
      return False

# sort function
def sort2(data):
    d = copy.deepcopy(data)
    for i in range(len(data)):
        d[i] = sorted(d[i])

    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            try:
                re = gt(d[j],d[j+1])
            except:
                print "plz same row and col"
                return
            if re:
                temp = d[j]
                d[j] = d[j+1]
                d[j+1] = temp
    return d

# print sort2(r1)
# print sort2(r2)
