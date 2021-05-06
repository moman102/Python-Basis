with open("test.txt", "r") as file:
    data = file.read()

print(data)

name = input("name : ")
age = input("age : ")

with open("write.txt", "a+") as f:
    f.write(f"{name} is {age} years old\n ")
