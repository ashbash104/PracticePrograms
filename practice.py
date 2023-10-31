# number = input("Enter a 2 digit number: ")
# num1 = number[0]
# num2 = number[1]
# result = int(num1) + int(num2)
# print(result)
val1 = 7
val2 = 7
def add(val1, val2):
    if val2 == 0:
        return val1
    else:
        return 1 + add(val1, val2 - 1)
add(val1, val2)
print(add(val1, val2))

def funct(x, y):
    if x == 0:
        return 1
    else:
        return y + funct(x - 1, y)
funct(5, 3)
print(funct(5, 3))
