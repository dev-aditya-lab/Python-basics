# this is the programm to find the power of a number using closures
# closers are functions that return other functions



def chaicoder(num):
	def actual(x):
		return x ** num
	return actual

f = chaicoder(2)
g = chaicoder(3)
print(f(3))
print(g(3))

