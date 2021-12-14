def decoratorr():
	def wrapper(fn):
		print("Before")
		fn()
		print("After")

	return wrapper

# @decoratorr
def hello_world():
	print("hello_world")

hello_world()


decoratorr()(hello_world)

def route(url):
	wrapper(fn):
		validate_url(url)
		fn()
	return wrapper

