class pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

ob1 = pet("dog", 4)
ob2 = pet("cat", 3)
ob3 = pet("bird", 5)

print("{} is {} years old.".format(ob1.name, ob1.age))
print("{} is {} years old.".format(ob2.name, ob2.age))
print("{} is {} years old.".format(ob3.name, ob3.age))