numbers = [5, 6, 10, 67, 45, 2432, 56, 34, 342, 2342, 978]

def square(x):
    return x * x

numbers2 = list(map(square, numbers))

print(numbers2)

creature_names = ['Samoli', 'Ashloy', 'Jo', 'Olly', 'Jackie', 'Charlie']

def rep_s(name: str):
    return name.upper().replace("O", "*")

repl = map(rep_s, creature_names)
print(list(repl))
