class Verbose:
	def __init__(self, f):
		print "Initialize..."
		self.func = f
		self.count = 0

	# Python decorator takes "callable" object
	# Make this class callable
	def __call__(self):
		print "Begin", self.func.__name__
		self.func()
		self.count += 1
		print "End", self.func.__name__, "with count = ", str(self.count)

@Verbose
def foo():
	print "Hello, World"

@Verbose
def bar():
	print "Bye, World"

foo();
foo();
foo();
foo();
foo();

bar();
bar();