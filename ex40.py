#coding=utf-8
"""字典"""
cities = {'CA':'San Francisco','MI':'Detorit','FL':'Jacksonwille'}
cities['NY'] = 'New York'
cities['OR'] = 'porland'

def find_city(themap,state):
	if state in themap:
		return themap[state]
	else:
		return "Not find"
		
#ok pay attention!
cities['_find'] = find_city

while True:
	print "State? (Enter to quit)",
	state = raw_input("> ")
	
	if not state: break
	
	#this line is the most important ever! study!
	city_found = cities['_find'](cities,state)
	print city_found