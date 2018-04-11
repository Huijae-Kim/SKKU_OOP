l_b = [1,2,5,4,3,6,7]
print sorted(l_b)
l_c = sorted(l_b)
l_c.reverse()
print l_c
print l_c[::-1]
#l_d = l_b.sort().reverse()
#print l_d
print l_b[:4]

d_age = {'josang': 25, 'heejae': 26}
d_id = {'josang': 'boyfriend', 'heejae': 'girlfriend'}
print d_age['heejae']
print d_id['josang']
print d_age.keys()
print d_age.values()
print d_id.keys()
print d_id.values()

l_a = [1,2,2,3,3,3]
print set(l_a)
print set((1,2,3,4,3))

a=0
while a<10:
	a=a+1
	print "a="+str(a)

b=0
while True:
	if b<10:
		b=b+1
		print "b="+str(b)
	else:
		break


import random


number = random.randint(0,100)
while True:
	guess = int(raw_input("enter your guess integer: "))
	if guess < number:
		print "your number is smaller than the number"
		continue
	elif guess > number:
		print "your number is bigger than the number"
		continue
	else:
		print "your number is equal to the number!"
		break
print "game is finished"


for i,iv in enumerate("heejae loves josang"):
	print "id: {} - value: {}".format(i,iv)
	
l_d = [1,2,3,4,5]
l_e = ["a","b","c","d","e"]

for d,e in zip(l_d,l_e):
	print "id:{} - value: {}".format(d,e)
	
def add(a,b):
	c=a+b
	return c

print add(2,3)

c=100
def add2(a,b):
	global c
	d=a+b+c
	return d

print add2(2,30)

l_heejae = "heejae kim loves sangyeon cho".split(" ")
for i,iv in enumerate(l_heejae):
	print "id: "+str(i+1)+", value: "+iv


input = [1,2,3,4,5]

print range(len(input))

for i in range(len(input)):
	print i
	print input[i]
	

