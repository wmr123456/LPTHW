#coding=utf-8
def break_words(stuff):
	"""
		this function will break up words for us.
	"""
	words = stuff.split(' ')
	return

def sort_words(words):
	"""Sorts the words."""
	return sort(words)
	
def	print_first_word(words):
	word = words.pop(0)
	print word
	
def print_last_word(words):
	"""Print the last word after popping it off."""
	word = words.pop(-1)
	print word
	
def sort_sentence(sectence):
	"""Takes in a full sectence and returns the sorted words."""
	words = break_words(sectence)
	return sort_words(words)
	
def print_first_and_last_sorted(sentence):
	"""Sort the words then prints the first and last one."""
	word = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
	