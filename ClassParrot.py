class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

ob1 = Parrot("Blu", 10)
ob2 = Parrot("Woo", 15)

print("Blu is a", ob1.species, "\nWoo is also a", ob2.species)
print("{} is {} years old.".format(ob1.name, ob1.age))
print("{} is {} years old.".format(ob2.name, ob2.age))