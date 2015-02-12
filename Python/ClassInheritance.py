def tag(func):
    def calc(self):
        return func(self) + "(aaa)"
    return calc


class Foo():
	def __init__(self):
		self.x = 1
		self.y = 2

	@tag
	def foo(self):
		return "Hello, World"

foo = Foo()
print foo.foo()

class Bar(Foo):
	pass

	@tag
	@tag
	def foo(self):
		return "Bar, World"

bar = Bar()
print bar.foo()