import requests

try:
	r = requests.get("http://udacity.com")
	print(r.status_code)
except requests.exceptions.ConnectionError:
	print("Could not connect to server.")