import requests

r = requests.get("http://127.0.0.1:5000/time")
print("The current time is {}".format(r.json()))

r = requests.get("http://127.0.0.1:5000/date")
print("The current date is {}".format(r.json()))

out_json = {"date": "02/28/1999", "units": "years"}
r = requests.post("http://127.0.0.1:5000/age",
                  json=out_json)
days = r.json()
years = days / 365
print("Canyon is {} years old".format(years))

r = requests.get("http://127.0.0.1:5000/until_next_meal/breakfast")
print(r.json())

r = requests.get("http://127.0.0.1:5000/until_next_meal/lunch")
print(r.json())

r = requests.get("http://127.0.0.1:5000/until_next_meal/dinner")
print(r.json())
