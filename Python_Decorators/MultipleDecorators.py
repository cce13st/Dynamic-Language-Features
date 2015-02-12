# Decorator which makes negative return value to zero
def deco1(func):
    def calc(x):
    	print "Deco1"
        result = func(x)
        if result < 0:
            result = 0
        return result
    return calc

def deco2(func):
	def calc(x):
		print "Deco2"
		result = func(x)
		if result > 10:
			result = 10
		return result
	return calc

@deco1
@deco2
def foo(x):
    return x + 42
    
@deco1
@deco2
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
