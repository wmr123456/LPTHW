#coding=utf-8
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Firl","Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()	#移除最后一个元素并返回元素的值
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
	
print "There we go:", stuff

print stuff[1]
print stuff[-1] #whoa fancy
print ' '.join(stuff) #what cool!
print stuff[3:5] #输出stuff下标为3到5的元素，前闭后开
print '#'.join(stuff[3:5]) #super stllar!	#获取stuff的3,4两个元素，并用stuff[3]+'#'+stuff[4]组成一个字符串
print stuff
print '#'.join(stuff)	#获取stuff的所有元素在每两个元素中间添加'#'结果：Apples#Oranges#Crows#Telephone#Light#Sugar#Boy#Firl#Banana#Corn