
with open("hello_new.txt", "r", encoding="UTF-8") as fp:
    info = fp.read()
    print(info)
sum = 0

while sum <= 10:
    with open("hello.txt", "a", encoding="UTF-8") as fp:
        fp.write("Hello world!\n")
        fp.write("It`s Python\n")
        fp.write("I am developer\n")
        fp.write(str(sum))
        sum = sum + 1

with open("hello_new.txt", "r", encoding="UTF-8") as fp:
    info = fp.readlines()
    print(info)
print(len(info))
info2 = []
for i in info:
    info2.append(i.replace("\n", "").strip())

print(info2)

