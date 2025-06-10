fruits = {"яблуко", "банан", "апельсин", "яблуко", "банан", "молоко", "молоко"}
print(fruits)
fruits.add("цукор") #додає єлемент
print(fruits)
fruits.remove("цукор") #видаляє але може викликати помилку якщо значення немає
print(fruits)
fruits.discard("банан") #видаляє
fruits.discard("банан") #видаляє
print(fruits)

numbers = "1234554321"
new_numbers = set(numbers)
name = set("Andriy")
print(new_numbers)
print(name)