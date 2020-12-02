import datetime

def datetime_deco(func):
    def decorated():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return decorated

@datetime_deco
def func_1():
    print("Main Function 1 start")

@datetime_deco
def func_2():
    print("Main Function 2 start")

@datetime_deco
def func_3():
    print("Main Function 3 start")

func_1()
func_2()
func_3()
