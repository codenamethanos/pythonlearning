my_list = ["Nifal", "Hareb", "Ali", "Mohammed", "Ali"]
unique = []
for item in my_list:
    if item not in unique:
        unique.append(item)
print(unique)


# Unpacking for both lists and tuples
coordinates = (1, 2, 3)
x, y, z = coordinates

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"]) 
print(customer.get("name", "Default Value"))


try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value")

try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0") 
except ValueError:
    print("Invalid value")