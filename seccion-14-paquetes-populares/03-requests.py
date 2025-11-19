# API REST
# API  = Application Programming Interface
# REST = Representational State Tranfer

# https://jsonplaceholder.typicode.com/
# GET       https://jsonplaceholder.typicode.com/users   status code = 200
# GET       https://jsonplaceholder.typicode.com/users/5 status code = 200
# POST      https://jsonplaceholder.typicode.com/users   status code = 201
# PUT|PATCH https://jsonplaceholder.typicode.com/users/5 status code = 204
# DELETE    https://jsonplaceholder.typicode.com/users/5 status code = 204

import os
import requests 

url = "https://jsonplaceholder.typicode.com/users"

os.system('cls' if os.name == 'nt' else 'clear')
r = requests.get(url, timeout=10)
# print(r.status_code)
# print(r.text)
r = r.json()
for user in r:
    # print(user["name"])
    pass

url = "https://jsonplaceholder.typicode.com/users/5"
r = requests.get(url, timeout=10)
r = r.json()
# print("\n", r)

url = "https://jsonplaceholder.typicode.com/users"
user = {
    "name": "Lionel Prats",
}
r = requests.post(url, timeout=10, data=user)
# print(r.status_code)

url = "https://jsonplaceholder.typicode.com/users/2"
user = {
    "name": "Lionel Prats",
}
r = requests.put(url, timeout=10, data=user)
# print(r.status_code)

url = "https://jsonplaceholder.typicode.com/users/2"
r = requests.delete(url, timeout=10)
print(r.status_code)

