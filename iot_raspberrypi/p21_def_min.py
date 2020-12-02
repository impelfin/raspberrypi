def min(a, b):
    if a > b:
        return b
    else:
        return a

a = input("Input First Number : ")
b = input("Input Second Number : ")
print("{}  vs {} : Max number = {} ".format(a, b, min(a, b)))