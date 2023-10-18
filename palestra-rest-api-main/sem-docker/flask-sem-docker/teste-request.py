import requests

url = "localhost:9999/produtos"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
