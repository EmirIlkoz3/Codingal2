import random
import string

password1 = random.randint(0, 11)
password2 = random.choice(string.ascii_letters)
password3 = random.randint(0, 11)
password4 = random.choice(string.ascii_letters)
password5 = random.randint(0, 11)
password6 = random.choice(string.ascii_letters)
print("Your random generated password is:", password1,password2,password3,password4,password5,password6)