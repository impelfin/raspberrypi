numbers = [0, 1, 2, 3, 4]
even2 = (2 * i for i in numbers)
print(even2)
print(even2.__next__())
print(even2.__next__())
print(sum(even2))

print(numbers)
numbers.reverse()
print(numbers)
