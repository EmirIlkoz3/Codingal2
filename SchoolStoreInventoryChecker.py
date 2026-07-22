items = ["pencil", "eraser", "notebook", "sharpner", "glue"]
stock_counts = [12, 0, 8, 5, 3]

inventory = {item: count for item, count in zip(items, stock_counts)}
print("Full inventory:", inventory)

instockitem = [item for item in items if inventory[item] > 0]
print("Items in stock:", instockitem)

chooseanitem = input("Witch item do you want to buy: ")
if chooseanitem not in inventory or inventory[chooseanitem] == 0:
    print(chooseanitem, "is out of stock")
    exit()

prices = [10, 5, 40, 15, 20]
markup = int(input("Enter the markup amount to add to every price: "))
markupprices = list(map(lambda p: p + markup, prices))
print("Markup Prices:", markupprices)

itemindex = items.index(chooseanitem)
choosenprice = markupprices[itemindex]
print("Price of", chooseanitem, "after markup:", choosenprice)
inventory[chooseanitem] = inventory[chooseanitem] - 1
print(chooseanitem, "purchased! Remaining stock:", inventory[chooseanitem])

print("")
print("=========SCHOOL STORE INVENTORY CHECKER=========")
print("Item bought:", chooseanitem)
print("Price paid:", choosenprice)
print("Updated inventory:", inventory)
print("================================================")