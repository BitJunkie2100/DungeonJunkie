import time


# Check out our official website!
# https://sites.google.com/view/dungeonjunkie

#ver. 2.1.4
# # # # # # # # # # # # # # #
#17/ 15 14\ # 9   7   8 # 1 #
# # #   #   # # #   # # #   #
#20 #16 #13  10   6 # 3   2 #
#   # / # # #   #   #   # # #
#19  18 #12  11 # 5   4 \ $ #
# # # # # # # # # # # # # # #

#Eighteen and Artrooms require key functions to enter!

def resetvars():
  rk = 0
  bk = 0
  ga = 0
  bcone = 0
  sk = 0
  st = 0
  sw = 0
  rn = 0
  fsone = 0
  return rk,bk,ga,bcone,sk,st,sw,rn,fsone


def dungeontwointro():
	print("Thank you for playing Dungeon Junkie! Dungeon Two is currently in development.")
	print("But in the meantime, join our Official Discord for updates and challenges!")
	print("Your continued support helps us make this dream a reality!")
	print("Thank you again!")
	print("~ The Dungeon Junkie Team")
	menu(rk,bk,ga,bcone,sk,st,sw,rn,fsone)

def artone(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           #           #   #
# # #   #   # # #   # # #   #
#   #   #           #       #
#   # 2 # # #   #   #   # # #
#       #       #       1 & #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
Dungeon One Completed!
	''')
	#200 points for completing the dungeon.
	#global fsone
	fsone = bk + rk + ga + bcone + 200
	print("Final Score: ",fsone)

	print("Press Enter to continue to Dungeon Two")
	
	c = input(">")
	
	dungeontwointro()
	
	

def twenty(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           #           #   #
# # #   #   # # #   # # #   #
# & #   #           #       #
#   # 2 # # #   #   #   # # #
#       #       #       1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go South(1)

-Examine Room(2)
	''')
	
	c = input(">")
	
	if c is "1":
		nineteen()
		
	elif c is "2":
		if bcone is 0:
			#global bcone
			print("You found the bonus chest! +500 points!")
			time.sleep(1)
			bcone = 500
			twenty(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
			
		elif bcone is 500:
			print("You've already collected the bonus chest.")
			time.sleep(1)
			twenty(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
			
		else:
			print("Error. Internal Variable Contradiction")
		
	else:
		print("Command not found")
		time.sleep(1)
		twenty(rk,bk,ga,bcone,sk,st,sw,rn,fsone)

def nineteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           #           #   #
# # #   #   # # #   # # #   #
#   #   #           #       #
#   # 2 # # #   #   #   # # #
# &     #       #       1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go North(1)

-Go East(2)

-Examine Room(3)
	''')
	
	c = input(">")
	
	if c is "1":
		twenty(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		eighteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "3":
		print("You step awkwardly into the room. You're exhausted.")
		time.sleep(1)
		nineteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	else:
		print("Command not found")
		time.sleep(1)
		nineteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
def eighteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           #           #   #
# # #   #   # # #   # # #   #
#   #   #           #       #
#   # 2 # # #   #   #   # # #
#     & #       #       1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go North(1)

-Go West(2)

-Examine Room(3)
	''')
	
	c = input(">")
	
	if c is "1":
		sixteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		nineteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "3":
		print("The room smells like old wood. There's a chest nearby.")
		time.sleep(1)
		eighteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	else:
		print("Command not found")
		time.sleep(1)
		eighteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)

def seventeen(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
# &         #           #   #
# # #   #   # # #   # # #   #
#   #   #           #       #
#   # 2 # # #   #   #   # # #
#       #       #       1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go East(1)

-Examine Room(2)
	''')
	
	c = input(">")
	
	if c is "1":
		fifteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		if rk is 0:
			#global rk
			print("Wedged between two of the cold bricks in the wall is a red key. You yank it out.")
			time.sleep(1)
			print("Red Key (2) Collected!")
			rk = 50
			time.sleep(1)
			seventeen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
		elif rk is 50:
			print("The Red Key (2) has already been collected.")
			time.sleep(1)
			seventeen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
			
		else:
			print("Error - Internal Variable Contradiction")
			
	else:
		print("Command not found")
		time.sleep(1)
		seventeen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)

def sixteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           #           #   #
# # #   #   # # #   # # #   #
#   # & #           #       #
#   # 2 # # #   #   #   # # #
#       #       #       1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go South(1)

-Go North(2)

-Examine Room(3)
	''')
	
	c = input(">")
	
	if c is "1":
		if rk is 50:
			eighteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
			
		elif rk is 0:
			print("The door is locked. You need the Red Key (2)")
			time.sleep(1)
			sixteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		fifteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "3":
		print("Another skeleton is shackled to the wall. The difference? You swear that this one moved")
		time.sleep(1)
		sixteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	else:
		print("Command not found")
		time.sleep(1)
		sixteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)

def fifteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#     &     #           #   #
# # #   #   # # #   # # #   #
#   #   #           #       #
#   # 2 # # #   #   #   # # #
#       #       #       1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go East(1)

-Go South(2)

-Go West(3)

-Examine Room(4)
	''')
	
	c = input(">")
	
	if c is "1":
		fourteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
	
	elif c is "2":
		sixteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "3":
		seventeen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "4":
		print("Fountains. There's a fountain for every corner of the room. Strange.")
		time.sleep(1)
		fifteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	else:
		print("Command not found")
		time.sleep(1)
		fifteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)

def fourteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#         & #           #   #
# # #   #   # # #   # # #   #
#   #   #           #       #
#   # 2 # # #   #   #   # # #
#       #       #       1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go South(1)

-Go West(2)

-Examine Room(3)
	''')
	
	c = input(">")
	
	if c is "1":
		thirteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		fifteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "3":
		if bk is 0:
			#global bk
			print("You walk into the room and instantly get dizzy. It's so...familiar. You balance yourself and see a key sitting on a pedestal in front of you. You pick it up.")
			time.sleep(1)
			print("Blue Key (1) Collected!")
			time.sleep(1)
			bk = 50
			fourteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
		elif bk is 50:
			print("The Blue Key (1) has already been collected.")
			time.sleep(1)
			fourteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)

	else:
		print("Command not found")
		time.sleep(1)
		fourteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
		
def thirteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           #           #   #
# # #   #   # # #   # # #   #
#   #   # &         #       #
#   # 2 # # #   #   #   # # #
#       #       #       1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go North(1)

-Go East(2)

-Examine Room(3)
	''')
	
	c = input(">")
	
	if c is "1":
		fourteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		ten(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "3":
		print("The room quakes when you step. Very unstable. You should finish up in here quickly.")
		time.sleep(1)
		thirteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
	
	else:
		print("Command not found")
		time.sleep(1)
		thirteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)

def twelve(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           #           #   #
# # #   #   # # #   # # #   #
#   #   #           #       #
#   # 2 # # #   #   #   # # #
#       # &     #       1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go East(1)

-Examine Room(2)
	''')
	
	c = input(">")
	
	if c is "1":
		eleven(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		print("You lean into the wall. It's like it bends inwards. You're about touch the brick, but two yellow eyes open in front of you.")
		time.sleep(1)
		twelve(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	else:
		print("Command not found")
		time.sleep(1)
		twelve(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
	
def eleven(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''	
# # # # # # # # # # # # # # #
#           #           #   #
# # #   #   # # #   # # #   #
#   #   #           #       #
#   # 2 # # #   #   #   # # #
#       #     & #       1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go North(1)

-Go West(2)

-Examine Room(3)
	''')
	
	c = input(">")
	
	if c is "1":
		ten(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		twelve(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "3":
		print("You stroll into the room, almost stepping into a pit of quicksand.")
		time.sleep(1)
		eleven(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	else:
		print("Command not found")
		time.sleep(1)
		eleven(rk,bk,ga,bcone,sk,st,sw,rn,fsone)

def ten(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           #           #   #
# # #   #   # # #   # # #   #
#   #   #     &     #       #
#   # 2 # # #   #   #   # # #
#       #       #       1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go East(1)

-Go South(2)

-Go West(3)

-Examine Room(4)
	''')
	
	c = input(">")
	
	if c is "1":
		six(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		eleven(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "3":
		thirteen(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "4":
		print("A single pint of mead sits on a cold, stone table. The cobwebs tell you it's aged to perfection. ")
		time.sleep(1)
		ten(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	else:
		print("Command not found")
		time.sleep(1)
		ten(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
def nine(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           # &         #   #
# # #   #   # # #   # # #   #
#   #   #           #       #
#   # 2 # # #   #   #   # # #
#       #       #       1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go East(1)

-Examine Room(2)
	''')
	
	c = input(">")
	
	if c is "1":
		seven(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		print("There's a small chest in the middle of the room. You choose not to open it out of paranoia.")
		time.sleep(1)
		nine(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	else:
		print("Command not found")
		time.sleep(1)
		nine(rk,bk,ga,bcone,sk,st,sw,rn,fsone)

def eight(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           #         & #   #
# # #   #   # # #   # # #   #
#   #   #           #       #
#   # 2 # # #   #   #   # # #
#       #       #       1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go West(1)

-Examine Room(2)
	''')
	
	c = input(">")
	
	if c is "1":
		seven(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		print("You find a small hamster, running in his wheel. What the actual hell is going on?")
		time.sleep(1)
		eight(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	else:
		print("Command not found")
		time.sleep(1)
		eight(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		

def seven(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           #     &     #   #
# # #   #   # # #   # # #   #
#   #   #           #       #
#   # 2 # # #   #   #   # # #
#       #       #       1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go East(1)

-Go West(2)

-Go South(3)

-Examine Room(4)
	''')
	
	c = input(">")
	
	if c is "1":
		eight(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		nine(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
	
	elif c is "3":
		six(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "4":
		print("Large stones form a line against the wall. You're descending deeper into the dungeon")
		time.sleep(1)
		seven(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	else:
		print("Command not found")
		time.sleep(1)
		seven(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
def six(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           #           #   #
# # #   #   # # #   # # #   #
#   #   #         & #       #
#   # 2 # # #   #   #   # # #
#       #       #       1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go North(1)

-Go South(2)

-Go West(3)

-Examine Room(4)
	''')
	
	c = input(">")
	
	if c is "1":
		seven(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		five(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "3":
		ten(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "4":
		print("You examine the strange markings on the walls of the dungeon. They don't look egyptian in origin, but something similar")
		time.sleep(1)
		six(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	else:
		print("Command not found")
		time.sleep(1)
		six(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
def five(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           #           #   #
# # #   #   # # #   # # #   #
#   #   #           #       #
#   # 2 # # #   #   #   # # #
#       #       # &     1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go North(1)

-Go East(2)

-Examine Room(3)
	''')
	
	c = input(">")
	
	if c is "1":
		six(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		four(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "3":
		print("The room smells of decay. You trip over the arm of a less-fortunate explorer.")
		time.sleep(1)
		five(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	else:
		print("Command not found")
		time.sleep(1)
		five(rk,bk,ga,bcone,sk,st,sw,rn,fsone)

def cheats():
	print("I don't think so. (-_- )")
	quit()
	
def four(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           #           #   #
# # #   #   # # #   # # #   #
#   #   #           #       #
#   # 2 # # #   #   #   # # #
#       #       #     & 1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go North(1)

-Go East(2)(Collect Artifact)

-Go West(3)

-Examine Room(4)
	''')
	
	c = input(">")
	
	if c is "1":
		three(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		if bk is 50:
			artone(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
			
		elif bk is 0:
			print("The door is locked. You need the Blue Key (1)")
			time.sleep(1)
			four(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "3":
		five(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "4":
		if ga is 0:
			#global ga
			print("You walk around the room. In the corner you find a Gauntlet. You put it on and a wave of power passes over you.")
			time.sleep(1)
			print("Gauntlet Collected!")
			ga = 100
			time.sleep(1)
			four(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
		elif ga is 100:
			print("The gauntlet has already been collected.")
			time.sleep(1)
			four(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
			
	else:
		print("Command not found")
		time.sleep(1)
		four(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
			

def three(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           #           #   #
# # #   #   # # #   # # #   #
#   #   #           # &     #
#   # 2 # # #   #   #   # # #
#       #       #       1 $ #
# # # # # # # # # # # # # # #
	''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go South(1)

-Go East(2)

-Examine Room(3)
	''')
	
	c = input("")
	
	if c is "1":
		four(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		two(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "3":
		print("You check all around the room. Nothing but a pile of bones in the corner. Gross.")
		time.sleep(1)
		three(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	else:
		print("Command not found")
		time.sleep(1)
		three(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		

def two(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           #           #   #
# # #   #   # # #   # # #   #
#   #   #           #     & #
#   # 2 # # #   #   #   # # #
#       #       #       1 $ #
# # # # # # # # # # # # # # #''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go West(1)

-Go North(2)

-Examine Room(3)
	''')
	
	c = input(">")
	
	if c is "1":
		three(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		one(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "3":
		print("The floor creaks when you step on it. Waterfalls collapse on the ground near the entrance.")
		time.sleep(1)
		two(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	
def one(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
# # # # # # # # # # # # # # #
#           #           # & #
# # #   #   # # #   # # #   #
#   #   #           #       #
#   # 2 # # #   #   #   # # #
#       #       #       1 $ #
# # # # # # # # # # # # # # #''')
	print("--------------------------------------------------------------------------------")
	print('''
-Go South(1)

-Examine Room(2)
	''')

	c = input("")

	if c is "1":
		two(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
	
	elif c is "2":
		print("The room smells like smoke. This is probably because you blew up the entrance, you bum.")
		time.sleep(1)
		one(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	else:
		print("Command not found")
		time.sleep(1)
		one(rk,bk,ga,bcone,sk,st,sw,rn,fsone)

def dungeononeintro(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print("Welcome to Dungeon Junkie - A Completely Text Based Dungeon Crawler")
	time.sleep(1)
	print("This is the first dungeon of the game. If you make your way through all 6 dungeons, you win.")
	time.sleep(1)
	print("Good Luck!")
	time.sleep(1)
	one(rk,bk,ga,bcone,sk,st,sw,rn,fsone)

def htp():
	print('''
Dungeon Junkie is a very easy game to play.
The only two skills you need are the ability to read and explore.
	
In each room of the dungeon you will be presented with options, either to
move to another room or examine the one you're in.
Simply entering the number corresponding to each option will select it 
and move you on.
	
Item Index:
1 - Blue Key (Blue Key needed)
2 - Red Door (Red Key needed) 
& - YOU
$ - The Artifact. Collecting this will end the dungeon.
The rest of the items are hidden and you must examine rooms to find them.
	
Simply follow the instructions on the screen and you'll do fine!
	''')
	time.sleep(2)
	menu(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
	
def credit():
	print("This game was designed and programmed by Cole Warren with original Concept Work and Pixel Art by Ian Eisenhower")
	print("This program was distributed to the public at no charge. If you paid money for this, you have been royally screwed.")
	print("Join our Discord Server and subscribe to our newsletter! (Link at the top of the source)")
	time.sleep(2)
	menu(rk,bk,ga,bcone,sk,st,sw,rn,fsone)

def quitgame():
	print("Are you sure you want to quit?")
	print("Y(1)/N(2)")
	
	c = input(">")
	
	if c is "1":
		quit()
		
	elif c is "2":
		menu(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	else:
		print("Command not found")
		time.sleep(1)
		quit()
		
def menu(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print('''
-Start Game(1)

-How To Play(2)

-Credits(3)

-Quit(4)
	''')

	c = input(">")

	
	if c is "1":
	 
	  dungeononeintro(rk,bk,ga,bcone,sk,st,sw,rn,fsone)
		
	elif c is "2":
		htp()
		
	elif c is "3":
		credit()
	
	elif c is "4":
		quitgame()
		
	elif c is "5":
		cheats()
	
	else:
		print("Command not found")
		time.sleep(1)
		menu(rk,bk,ga,bcone,sk,st,sw,rn,fsone)

def gamestart(rk,bk,ga,bcone,sk,st,sw,rn,fsone):
	print("Dungeon Junkie")
	print("ver. 2.1.4")
	print("Developed by Cole Warren")
	menu(rk,bk,ga,bcone,sk,st,sw,rn,fsone)


rk,bk,ga,bcone,sk,st,sw,rn,fsone = resetvars()
gamestart(rk,bk,ga,bcone,sk,st,sw,rn,fsone)