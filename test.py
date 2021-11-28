import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "user/1/pass123")
print(response.json())
response = requests.post(BASE + "mood/1/3")
print(response.json())
