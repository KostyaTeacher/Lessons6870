#key - value
#ключ - значення
#love - кохати
name  = "Kostya"
my_dict = { "name": "Alice",
            "age": 10,
            "city": "Wonderland"}


print(my_dict["city"])
print(my_dict.get("citys"))
answer = my_dict.get("city")
if answer is None:
    print("Данні не знайдено")
else:
    print(answer)

my_dict["weather"] = "sunny" #додати
print(my_dict)
my_dict["weather"] = "rainy" #додати
print(my_dict.get("weather"))
del my_dict["weather"] #видалити
print(my_dict)
my_dict.pop("age") #видалити
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
