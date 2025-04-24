person = {
    "name": "Fuad",
    "age": 23,
    "city": "Jashore"
}
print(person["name"])  # Fuad
print(person.get("city"))  # Jashore
print(person.get("country", "Bangladesh"))  # Bangladesh
print(person.get("country"))  # None
person.pop("city")  # removes 'city'
print(person)  # {'name': 'Fuad', 'age': 23}
person["age"] = 24  # updates 'age'

users = {
    "fuad": {"age": 23, "city": "Jashore"},
    "sami": {"age": 22, "city": "Dhaka"}
}

print(users["fuad"]["city"])  # Jashore
print(users["sami"]["age"])  # 22
print(users["fuad"].get("country", "Bangladesh"))  # Bangladesh