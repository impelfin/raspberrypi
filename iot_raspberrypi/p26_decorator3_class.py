import datetime

class DatetimeDecorator:
    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        print(datetime.datetime.now())
        self.func(*args, **kwargs)
        print(datetime.datetime.now())

class MainClass:
    @DatetimeDecorator
    def func_1():
        print("Main Function 1 start")
    @DatetimeDecorator
    def func_2():
        print("Main Function 2 start")
    @DatetimeDecorator
    def func_3():
        print("Main Function 3 start")

my = MainClass()
my.func_1()
my.func_2()
my.func_3()
