bestehquote = int(input(" bestehquote :  "))
note = int(input("student note :  "))

if note >= bestehquote:
    print("Bestanden !")

elif note < bestehquote:
    print("nicht bestanden !")


for i in range(1,51, 10):
    print(i)

string = "This is a String !"
tcount = 0
for char in string:
    if char.lower()=='t':
        tcount = tcount +1

print("t count is :" , tcount)

x = 0

while x <= 5:
    print(x)
    x = x + 1
isCharA = False

y = 0
while not isCharA :
    if string[y].lower() == 'a':
        print(f"A exist at Index {y}")
        isCharA = True
    else :
        y = y + 1
