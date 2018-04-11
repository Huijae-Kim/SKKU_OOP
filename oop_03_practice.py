hello = "hello, world! my name is heejae. I am 26 years old."

print hello.split(".")
print hello.split(".")[1]
print hello.split(".")[1].strip()
print repr(hello.split(".")[1].strip())
print hello[0:7]
print repr(hello[0:7])
print len(hello)
print hello.find('.')
print hello.rfind('.')
print hello[-4:]

name = 'heejaekim'
age = 26
hello2 = "hello, world! my name is {}. I am {} years old."
print hello2.format(name, age)

realNumber = 36
guessNumber = int(input("what is your guess number?"))

if guessNumber == realNumber:
	print "equal"
elif guessNumber > realNumber:
	print "your number is bigger"
else:
	print "your number is smaller"

print "done" 

number = float(raw_input("write float number : "))
print str(int(number))+", "+number-int(number)

