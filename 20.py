#!include /usr/env/python

if __name__ == "__main__":

	from math import factorial
	
	a = str(factorial(100))
	print sum(int(i) for i in a)
	


