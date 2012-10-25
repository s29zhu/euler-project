#!include /usr/env/python

from math import floor, ceil

if __name__ == '__main__':
	x = 0
	y = 1
	summation = 0
	while x < 4000000:
		summation += x
		a = x + 2*y
		b = 2*x+ 3*y
		x = a
		y = b
	print summation
