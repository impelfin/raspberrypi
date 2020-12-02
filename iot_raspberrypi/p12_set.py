even = set([0, 2, 4, 6, 8])
print(even)

hello =  set("Hello")
print(hello)

s = even | hello
print(s)

p = even & hello
print(p)

even.add(10)
print(even)

hello.remove('e')
print(hello)
