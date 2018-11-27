s = [1, 2]
v = ['a', 'b']

def myzip(first, second):
	for i in range(len(first)):
		yield first[i], second[i]

z = myzip(s, v)
print(next(z))
print(next(z))
print(next(z))