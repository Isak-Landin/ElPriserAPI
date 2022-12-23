import requests
import json

response = requests.post('https://isaklandin.com/api/prices/')

print(response.content)