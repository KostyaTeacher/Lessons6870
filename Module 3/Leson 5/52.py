multL = lambda a, b, c: a * b * c
print(multL(2, 5, 5))

#check_even = lambda x: x % 2 == 0

numbers = [5, 6, 10, 67, 45, 2432, 56, 34, 342, 2342, 978]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)