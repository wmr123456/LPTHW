#coding=utf-8
from sys import argv

script, input_file = argv

#读取文件输出
def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0) #将文件指针移动到文件开头
	
def print_a_line(line_count,f):
	#f.readline读取文件中一行的内容
	print line_count,f.readline() 
	
current_file = open(input_file)

	
print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

#确保文件从开头位置开始读取
rewind(current_file)

print "Let's print three linee:"

#/调用print_a_line函数输出行号和内容重复三遍
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)