import random

for i in range(3):
    print(random.random())
    print(random.randint(1, 10))

members = ["John", "Mary", "Hosh"]
print(random.choice(members))
