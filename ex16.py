#coding=utf-8
"""
	close 关闭文件
	read 读取文件内容，可以经内容复制给一个变量
	readline 读取文件中的一行
	truncate 清空文件，小心使用
	write(stuff) 将stuff内容写入文件
"""

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."
raw_input("?")
print "Opening the file..."
target = open(filename,'w')

print "Truncate the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:" )
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close file"
target.close()
