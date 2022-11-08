def fav_color():
	response = input("can you guess what my favorite color is?\n")
	if response == 'black':
		print("that's right!")
	else: 
		print("no. try again")
		fav_color()

fav_color()