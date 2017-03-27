#coding=utf-8
"""else if"""
people  = 30
cats = 40
buses = 15

if cats > people:
	print "We should takes the cars."
elif cats < people:
	print "We should not take the cars."
else:
	print "We can't decide."
	
	
if buses > cats:
	print "That's too many buses."
elif buses < cats:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."
	
if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."