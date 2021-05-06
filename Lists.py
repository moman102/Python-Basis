shoppingcart = ["apple ", "ananas ", "mangos", "bread"]
shoppingcart.pop(2)
print(shoppingcart)
shoppingcart.append("papaya")
print(shoppingcart)

shoppinglist = []
quit = False

while not quit:
    userInput = input("y to add more items , n to stop  :  ")
    if userInput.lower() == "y":
        item = input("enter item  :")
        shoppinglist.append(item)
    elif userInput.lower() == "n":
        quit = True
    else:
        print("Invalid input")

print("your shopping list contains : ", shoppinglist)

list = ["z","a" , "b" , "c" , "d"]
list.sort()
for item in list:
    if item == 'd':
        print(list.index('d'))
    print(item)

Alex = {
    "firstname ": "Alex ",
    "Matrikel nr ": "266186",
    "Age": "22",
    "sex":"M"
}

print(Alex["firstname "],Alex["Matrikel nr "])
Alex["Tel"] = "123456789"

print(Alex)

for n in Alex.values():
    print(n)
