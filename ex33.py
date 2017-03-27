#coding=utf-8
import ex33_f

"""
i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	i  += 1
	print "Number now: ", numbers
	print "At the bootom i is %d" % i
	
	
print "The number: "
for num in numbers:
	print num
"""
b = int(raw_input("please input a number: "))#注意将读入的信息转成int，否则函数会将读取的信息当成字符串处理!
print b
ex33_f.while_number(b)