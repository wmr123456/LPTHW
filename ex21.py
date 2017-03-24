#coding=utf-8
#加法
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

# 减法
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

#乘法
def multply(a, b):
	print "MULTILYING %d * %d" % (a,b)
	return a * b
	
#除法
def divide(a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a /b
	
print "Let's do some math with just function!"

age = add(30,5)
height = subtract(78,4)
weight = multply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age,height,weight,iq)

#A puzzle for the extra credid,type it in anyway.
print "Here is a puzzle."

what = add(age,subtract(height,multply(weight,divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"
