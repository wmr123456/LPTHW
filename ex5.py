my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %r." % my_name
print "He's %d inches tall." % my_height
print "He's %r pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teech are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it excactly right

print "if I add %r, %r and %r I get %r" % (my_age, my_height, my_weight, my_age + my_height + my_weight)