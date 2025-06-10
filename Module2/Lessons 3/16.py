import random as r
# random.random()	Повертає випадкове число з інтервалу [0.0, 1.0).
# random.randint(a, b)	Повертає випадкове ціле число в межах від a до b (включно).
# random.choice(seq)	Повертає випадковий елемент з непорожнього послідовності seq.
# random.shuffle(x)	Перемішує елементи списку x.
# random.sample(population, k)	Повертає k випадкових елементів з population.

print(r.random())
print(r.randint(1, 100))
name = ["Andriy", "Yaroslav", "Denis", "Kiril", "Roman"]
print(r.choice(name))
r.shuffle(name)
print(name)