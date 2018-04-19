import random
while True:
    random_num=random.randint(100,999)
    if str(random_num)[0]=="0" or str(random_num)[1]=="0" or str(random_num)[2]=="0" or str(random_num)[0]==str(random_num)[1] or str(random_num)[0]==str(random_num)[2] or str(random_num)[1]==str(random_num)[2]:
        continue
    else:
        break
print "welcome to baseball game.\nyour random number is {}.\n".format(random_num)
while True:
    guess_num=int(raw_input("enter your number :")) ; strike = 0 ; ball = 0
    for ri, rv in enumerate(str(random_num)):
        for gi, gv in enumerate(str(guess_num)):
            if ri==gi and rv==gv:
                strike += 1
            elif ri!=gi and rv==gv:
                ball += 1
    if strike == 3:
        print "you have the correct answer." ; break
    else:
        print "strike: {}, ball: {}".format(strike,ball) ; continue
