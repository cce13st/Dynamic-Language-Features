def genCls(cls):
	class rebuilder(cls):
		x = 2
		y = 5
		"This is the overwritten class"
		def __getattribute__(self, attr_name):
			obj = super(NewClass, self).__getattribute__(attr_name)

			return obj
	return rebuilder

@genCls
class Foo():
	def describe(self):
		return self.x

foo = Foo()
print foo.describe()
print foo.y