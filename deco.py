"""
def decorator(func):
    def decorated(*args, **kwargs):
        print("전처리")
        func()
        print("후처리")
    return decorated

@decorator
def exam():
    print("함수실행")

exam()
"""

class Decorator:
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("전처리")
        self.func()
        print("후처리")

@Decorator
def exam1():
    print("함수1실행")
@Decorator
def exam2():
    print("함수2실행")

exam1()
exam2()

