import requests

BASE_URL = "http://127.0.0.1:5000/resources"

# Create a resource
response = requests.post(BASE_URL, json={"name": "Oxygen Tanks", "quantity": 50})
print(response.json())

# Get all resources
response = requests.get(BASE_URL)
print(response.json())

# Get a single resource
response = requests.get(f"{BASE_URL}/1")
print(response.json())

# Update resource
response = requests.put(f"{BASE_URL}/1", json={"quantity": 75})
print(response.json())

# Delete resource
response = requests.delete(f"{BASE_URL}/1")
print(response.json())
