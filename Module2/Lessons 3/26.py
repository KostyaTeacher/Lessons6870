x = 10
print(x)

def abracadabra():
    y = 50 #local
    print(y)
    def abaracdadnra2():
        z = 100 #enclosing
        print(z)
    abaracdadnra2()

abracadabra()
print(x)
