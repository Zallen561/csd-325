import requests

# Test connection
response = requests.get("http://www.google.com")
print("Connection test status code:", response.status_code)

import requests
import json

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)
print("Status Code:", response.status_code)

print("\nRaw Response:")
print(response.text)

print("\nFormatted Response:")
data = response.json()
print(json.dumps(data, indent=4))

print("\nPeople in space right now:")
for person in data["people"]:
    print(f"- {person['name']} on {person['craft']}")
