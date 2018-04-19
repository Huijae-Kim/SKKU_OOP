import copy
from oop_07_class_1 import sort2

# open the file
fp = open("oop_07_data_1.csv", "r") #file pointer(file location)
# line1 = fp.readline() # one line by step, until EOF(end of file)
# print line1
# line2 = fp.readline() # cursor is moving
# print line2

lines = fp.readlines() # readlines from cursor to EOF
print lines
print type(lines) # check data type

fp.close() # i'm done...?!

d1 = []
for line in lines:
    d1.append(line[:-1])

print d1

for ri in range(len(d1)):
    tt = d1[ri].split(',')
    ttt =[]
    for dd in tt:
        try:
            ttt.append(int(dd))
        except:
            print "File has non-digit value"
            import sys
            sys.exit() # program off
    d1[ri] = copy.deepcopy(ttt)
print "d1 = ", d1

print "sort2(d1) = ", sort2(d1)

w_string = []
for i in d1:
    tmp_str = ''
    for ji, jv in enumerate(i):
        if ji == 0:
            tmp_str = tmp_str + str(jv)
        elif ji == len(i) -1 :
            tmp_str = tmp_str + "," + str(jv) + '\n'
        else:
            tmp_str = tmp_str + "," + str(jv)
    w_string.append(tmp_str)

print w_string

# make the csv file by coding
fp2 = open('oop_07_data_2.csv', 'w')
for line in w_string:
    fp2.write(line)

fp2.close() # you don't have to write it...but recommend to write down
