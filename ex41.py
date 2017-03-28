#coding=utf-8
from sys import exit
from random import randint

def death():
	quips = ["You died. You kinda suck at this.","Nice job,you died ... jackass.","Such a luser.","I have a small puppy that's better at this"]
	print quips[randint(0, len(quips)-1)]
	exit(1)

def central_corrodor():
	print "The Cothons of Planet Percal #25 have invaded your ship and destroyed"
	print "your entire crew. You are the last surviving member and your last"
	print "misssion is to get the neutorn destuct bomb from the Weapons Armory,"
	print "put it in the bridge,and blow the ship up agter getting into an "
	print "escape pod."
	print "\n"
	print "You're running down the central corridor to the Weapons Armory when"
	print "a Gothon jumps out,red scaly skin,dark grimy teeth,and evil clown costume"
	print "flowing around his hate filled body. he's blocking the door to the"
	print "Armory and about to pull a weapon to blast you."
	
	action = raw_input("> ")
	
	if action == "shoot":
		print "Quick on the draw you yank out your blaster and fire it at the Gothon."
		print "His clown costume is flowing and moving around his body,which throws"
		print "off your aim. Your laster hits costume but misssion him entitrely. This"
		print "completely ruins his brand new costume his mother bought him,which"
		print "make him fly into an insane rage and blast you repeatedly in the face until"
		print "you are dead. Then he eats you."
		return 'death'
	elif action == "dodge!":
		print "Like a world class boxer you dodge, weave,ship and slide right"
		print "as the Gothon's blaster cranks a laser past your head."
		print "In the middle of your artful dodge your foot slips and you."
		print "bang your head on the metal wall and pass out."
		print "You wake up shortly agter only to die as the Cothons stomps on"
		print "your head and eats you."
		return 'death'
	elif action == "tell a joke":
		print "Lucky for you they made you learn Cothons insults in the academy."
		print "You tall the one Gothon joke you know:"
		print "Lbhe zbgure vf fb sog,jura fur fvgf nebhaq gur ubhfr,fur fvgf nebhaq gur ubhf"
		print "The Gothon stops,tries not to laugh,then busts out laughing and can't move."
		print "putting him down,then jump through the Weapon the Armory door."
		return 'last_weapon_armory'
	else:
		print "DOES NOT COMPUTE!"
		return 'central_corrdidor'
def last_weapon_armory():
	print "You do a dive roll into the Weapon Armory,crouch and scan the room"
	print "for more Gothon that might be hiding. It's dead quiet,too quiet."
	print "You stand up and run to the far side of the room and find the"
	print "neutorn bimb in its container.There's a keyypad lock on the box"
	print "and you need the code to get the bomb out. If you get the code"
	print "wrong 10 times then the lock is closes forwver and you can't"
	print "get the bomb. The code is 3 digits."
	code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
	guess = raw_input("[keypad]> ")
	guesses = 0
	while guesses != code and guesses < 10:
		print "BZZZZEDD!"
		guesses +=10
		guess = raw_input("[keypad]> ")
		
	if guess == code:
		print "The container clicks open and the seal breaks, letting gas out."
		print "You grppb where you must place it in the right spot."
		return 'the_bridge'
	else:
		print "The lock buzzes one last time and then you ear a sickening"
		print "neting ound as the mechaism is fused togher."
		print "You decide to sit there,and finally the Gothons blow up the"
		print "ship from their ship and you die."
		return 'death'
	
def the_bridge():
	print "You urst onto the Bridge with the neutorn destruct bomb"
	print "under your arm and surprise 5 Cothons who are trying to"
	print "take control of the ship . Eacg if them has an even uglier"
	print "weapon out yet, as they see the active bomb under your"
	print "arm and don't want to set it off."
	action = raw_input("> ")
	
	if action == "thtow the bomb":
		print "In a panic you throw the bomb at the group of Gothons"
		print "and make a leap for the door. Right ad you dorp it a"
		print "Gothon shoots you right in the baack killing you."
		print "As you die you see another Cothon frantically try too disarm"
		print "the bomb,You die knowing they will pribably blow up then"
		print "it goes off."
		return 'deach'
	elif action == "slowly place the bomb":
		print "You point your blaster at the bomb under your arm"
		print "and the Gothons put their bads up and start to sweat."
		print "You inch backward to the door, open it, and then carefully"
		print "place the bomb on the floor, pointing your blaster at it."
		print "You then jump back through the door, punch the close button"
		print "and blast the lock so the Gothons can't get out."
		print "Now that the bomb is placed you run to the escape pod to"
		print "get off this tin can."
		return 'escape_pod'
	else:
		print "DOES NOT COMPUTE!"
		return "the_bridge"
def escape_pod():
	print "You rush through the ship desperately trying to make it to"
	print "the escape pod before the whole ship explodes. It seems like"
	print "hardly any Gothons are on the ship, so your run is clear of"
	print "interference. You get to the chamber with the escape pods, and"
	print "now need to pick one to take. Some of them could be damaged"
	print "but you don't have time to look. There's 5 pods, which one"
	print "do you take?"
	
	good_pod = randint(1,5)
	guess = raw_input("[pod #]> ")
	
	if int(guess) != good_pod:
		print "You jump into pod %s and hit the eject button." % guess
		print "The pod escapes out into the void of space, then"
		print "implodes as the hull ruptures, crushing your body"
		print "into jam jelly."
		return 'death'
	else:
		print "You jump into pod %s and hit the eject button." % guess
		print "The pod easily slides out into space heading to"
		print "the planet below. As it flies to the planet, you look"
		print "back and see your ship implode then explode like a"
		print "bright star, taking out the Gothon ship at the same"
		print "time. You won!"
		exit(0)
		
		
		
ROOMS = {
	'death' : death,
	'central_corrodor' : central_corrodor,
	'last_weapon_armory' : last_weapon_armory,
	'the_bridge' : the_bridge,
	'escape_pod' : escape_pod
}

def runner(map, start):
	next = start
	
	while True:
		room = map[next]
		print "\n-------"
		next = room()
		
runner(ROOMS,'central_corrodor')