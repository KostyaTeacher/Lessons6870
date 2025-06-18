my_list = []

numbers = [1, 2, 3, 4, 5]

fruits = ["apple", "banana", "kiwi", "orange", "watermelon"]

other = [23, True, "Kostya", {5, 10, 15}]

print(fruits)
sum = 0
for number in numbers:
    sum = sum + number
    #sum += number
    print(number)
print(sum)
for fruit in fruits:
    print(fruit.upper())

