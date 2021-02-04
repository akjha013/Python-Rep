# dictionary
customer ={
    "name": 'Jane Doe',
    "age": 40,
    "is_verified": True
}
print(customer["name"])
print(customer.get("city","delhi"))

customer["city"] = 'noida'
print(customer.get("city","delhi"))
print(customer)