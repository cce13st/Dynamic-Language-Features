# Decorator which makes negative return value to zero
def bound(func):
    def calc(x):
        result = func(x)
        if result < 0:
            result = 0
        return result
    return calc

@bound
def foo(x):
    return x + 42
@bound
def bar(x):
    return x - 42


print foo(-100)
print foo(2)
print bar(100)
print bar(2)

'''
Result of Python interpreter

0
44
58
0

'''
