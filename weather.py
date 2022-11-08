import requests
r = requests.get("https://example.net/api")
j = r.json()
print(f"I have {j['worries']} worries and {j['programs']} programs.")