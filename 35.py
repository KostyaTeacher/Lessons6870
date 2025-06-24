for i in range(1, 10):
    if i == 5:
        continue
    for j in range(1, 10):
        if j == 5:
            continue
        for k in range(1, 10):
            if k == 5:
                continue
            print(f"{i} x {j} x {k} = {i * j * k}")

while True:
    answer = input(" >")
    if answer == "exit":
        break