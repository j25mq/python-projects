def get_foo():
	response = input('say "foo"!')
	if response != 'foo':
		get_foo()

get_foo()