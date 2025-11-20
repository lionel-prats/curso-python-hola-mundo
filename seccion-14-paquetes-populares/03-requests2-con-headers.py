import os
import requests 

os.system('cls' if os.name == 'nt' else 'clear')

url = "https://jsonplaceholder.typicode.com/users"

apikey = "123456"
headers = {
    "Authorization": f"Bearer {apikey}"
}

r = requests.get(url, timeout=10, headers=headers)

url = "https://jsonplaceholder.typicode.com/users/5"
r = requests.get(url, timeout=10, headers=headers)
r = r.json()
print(r)

url = "https://jsonplaceholder.typicode.com/users"
user = {
    "name": "Lionel Prats",
}
r = requests.post(url, timeout=10, data=user, headers=headers)
# print(r.status_code)

url = "https://jsonplaceholder.typicode.com/users/2"
user = {
    "name": "Lionel Prats",
}
r = requests.put(url, timeout=10, data=user, headers=headers)
# print(r.status_code)

url = "https://jsonplaceholder.typicode.com/users/2"
r = requests.delete(url, timeout=10, headers=headers)
# print(r.status_code)