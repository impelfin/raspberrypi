import calc_class

a = int(input('Input First Number : '))
b = int(input('Input Second Number : '))

my = calc_class.Calc(a, b)

print('{} + {} = {} '.format(a, b, my.add()))
print('{} - {} = {} '.format(a, b, my.sub()))