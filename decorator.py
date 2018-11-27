import time

def decorator(func):

	def fake(value):
		start = time.clock()
		result = func(value)
		end = time.clock()
		print('Time is', end - start)
		return result
	
	return fake #func

@decorator
def my_str(value):
    return str(value)

#fake = decorator(str)
#my_str = decorator(my_str)
#print(fake(123))
print(my_str(123))
print(my_str([]))
print(my_str({}))