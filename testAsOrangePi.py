import requests

response = requests.get('https://isaklandin.com/prices')

response = response.json()
print(response)
