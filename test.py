import requests

BASE = "http://127.0.0.1:5000/"

# create user
response = requests.post(BASE + "user/1/pass123")
print(response.json())

# post mood
response = requests.post(BASE + "mood/1", {"mood": 3})
print(response.json())

# get mood
response = requests.get(BASE + "mood/1")
print(response.json())
