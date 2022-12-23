import requests
import json

response = requests.post('http://api.isaklandin.com/prices/')
print(response.json())
