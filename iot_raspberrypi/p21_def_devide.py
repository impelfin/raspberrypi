def divide(a, b):
        return (a / b, a % b)

a = input("Input First Number : ")
b = input("Input Second Number : ")

#print("Input number %d / %d " % (int(a), int(b)))
#print("Input number {} / {} ".format(a, b))
print(f'Input number {a} / {b}')
q, r = divide(int(a), int(b))

print("Quotient : ", q)
print("Remainder : ", r)
