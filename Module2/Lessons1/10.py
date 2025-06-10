# answer = float(input("Input number a "))
# answer2 = float(input("Input number b "))
#
# print(answer * answer2)
# int
# float
# bool
# str
name = ("""
1 питання
Як звали Кобзаря:
1. Денис
2. Олег
    """)
# len(рядок) - повертає довжину рядка
# рядок.upper() - перетворює всі літери на великі
# рядок.lower() - перетворює всі літери на малі
# рядок.replace(стара_частина, нова_частина) -
# змінює "стару" частину в рядку на нову
print(len(name))
print(name.upper())
print(name.lower())
print(name)
name = (name.replace("\n", "").
         replace(" ", "").upper())
print(name)
print(name)
print(name)

