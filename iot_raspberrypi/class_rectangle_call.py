from class_ex import *

square1 = Rectangle.isSquare(5, 5)
print(square1)

rect1 = Rectangle(5, 5)
print('Area of rect1 is ', rect1.calcArea())

rect2 = Rectangle(2, 5)
print('Area of rect2 is ', rect2.calcArea())

rect3 = rect1 + rect2
print('Area of rect3 is ', rect3.calcArea())
rect3.width = 6
rect3.height = 6
print('Area of rect3 is ', rect3.calcArea())
