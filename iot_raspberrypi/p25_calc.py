def calc(a):
    def add(b):
        return a + b
    return add

sum = calc(1)
print(sum(2))
