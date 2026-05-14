import requests
import json

url = "https://catfact.ninja/fact"

# Test connection
response = requests.get(url)
print("Status Code:", response.status_code)

# Raw response
print("\nRaw Response:")
print(response.text)

# Formatted response
print("\nFormatted Response:")
data = response.json()
print(json.dumps(data, indent=4))

print("\nCat Fact:")
print(f"- {data['fact']}")
