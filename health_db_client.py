import requests

x = {"name": "Canyon Duncan", "id": 103, "age": 21}
r = requests.post("http://127.0.0.1:5000/new_patient", json=x)
print(r.status_code)
print(r.text)