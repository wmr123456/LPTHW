#coding=utf-8
cities = {'CA':'San Francisco','MI':'Detorit','FL':'Jacksonwille'}
cities['NY'] = 'New York'
cities['OR'] = 'porland'

for key,value in cities.items():
	print 'key=',key,'value=',value
	
for x in cities.items():
	print x