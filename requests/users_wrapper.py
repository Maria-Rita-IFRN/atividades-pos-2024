import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

def list_users():
    response = requests.get(BASE_URL)
    return response.json()

def create_user(data):
    response = requests.post(BASE_URL, json=data)
    return response.json()

def read_user(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    return response.json()

def update_user(user_id, data):
    response = requests.put(f"{BASE_URL}/{user_id}", json=data)
    return response.json()

def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")
    return response.status_code == 200
