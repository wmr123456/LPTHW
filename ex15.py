#coding=utf-8

from sys import argv

scitpt, filename = argv

txt = open(filename)

print "type the filename again:"

file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()