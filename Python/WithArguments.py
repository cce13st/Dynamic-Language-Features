class Verbose:
	def __init__(self, f):
		print "Initialize..."
		self.func = f

	def __call__(self, *args, **kwargs):
		print "Begin", self.func.__name__
		self.func(*args, **kwargs)
		print "End", self.func.__name__

@Verbose
def foo(name):
	print "Hello, ", name

foo("John");
foo("Fred");