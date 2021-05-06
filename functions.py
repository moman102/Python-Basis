def areaOfTriangle(base, height):
    return base * height * 1 / 2


b = int(input("b  : "))
h = int(input("h  : "))

area = areaOfTriangle(b, h)
print(area)

def isPalendrome(var):
    if var == var[::-1]:
        return True
    else:
        return False

print(isPalendrome("refer"))
print(isPalendrome("refere"))
