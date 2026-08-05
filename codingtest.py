namesandscores = {"matt": 56 , "tom": 87 , "john": 79 , "alex": 99 , "alice": 34}

ask = input("Which student do you want to look for? ")
checking = namesandscores.get(ask)
print(checking)
if ask not in namesandscores:
    print("The name you are searching is not in the list. Please try again")