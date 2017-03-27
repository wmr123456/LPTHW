#coding=utf-8
"""循环和列表"""

the_count = [1,2,3,4]
fruits = ['apples', 'oranges', 'pear', 'apricots']
change = [1,'pernies', 2, 'dimes', 3, 'auarters']

#this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
	
#also we can go through mixed lists too
#notice we have use %r since we don't know what's in items
for i in change:
	print "I got %r" % i
	
#we can also build lists, first start with an empty one
elements = []

#then use th range function to do 0 to 5 counts
for i in range(0,6):#前闭后开
	print "Adding %d to the list." % i
	#append is a function that lists understand
	elements.append(i)
	
#now we can print them out too
for i in elements:
	print "Element was: %d" % i