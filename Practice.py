string = input("~ ")

chars=''
nums= []
total = 0
for char in string:
    if char.isdigit():
        nums.append(int(char))
        total += int(char)
    else:
        chars += char

print("nums : " , nums)
print("chars :" , chars)
print("total :",total)

