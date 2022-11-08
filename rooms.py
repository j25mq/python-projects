def green_room():
	print("You are in the green room")
	choose_room()

def blue_room():
	print("You are in the blue room")
	choose_room()

def choose_room():
	choice = input("would you like to go to the green or blue room?\n")
	if choice == 'green':
		green_room()
	elif choice == 'blue':
		blue_room()
	else: 
		print("I don't know what that is.")
		choose_room()

choose_room()
