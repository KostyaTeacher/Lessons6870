my_dict = {"name": "Alice",
           "age": 10,
           "city": "Wonderland"}

for key in my_dict:
    print(my_dict.get(key))

for key, value in my_dict.items():
    print(f"[{key}] -> {value}")
