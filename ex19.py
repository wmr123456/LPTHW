#coding=utf-8
def cheese_and_crachers(cheese_count, boxes_of_crackers):
	print "You have %d chesses!" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket,\n"
	


print "We can just give the function munbers directly:"
cheese_and_crachers(10,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_and_crackers = 50


cheese_and_crachers(amount_of_cheese,amount_and_crackers)


print "We can even do math inside too:"
cheese_and_crachers(10 + 20, 5 + 6)


print "And we can combine the two , variables and math:"
cheese_and_crachers(amount_of_cheese + 100, amount_and_crackers + 1000)