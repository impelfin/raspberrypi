m = 0
n = 1
def func():
    m = 0
    global n
    m += 1
    n += 1
func()
print("{} vs {}".format(m, n))
print(m, n)
