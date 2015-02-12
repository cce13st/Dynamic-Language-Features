def tag(tag_string):
	def tag_generator(func):
		def func_wrapper():
			return func() + "(" + tag_string + ")"
		return func_wrapper
	return tag_generator


@tag("aaa")
def foo():
	return "Hello, world!"

print foo()