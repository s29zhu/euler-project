#!include /usr/bin/python

from math import floor,sqrt

def simplify(numerator, denominator):
	maxi = 0
	s = set('')
	if numerator >= denominator:
		return s
	for i in range(1, numerator + 1):
		if (not denominator % i) and i > maxi and (not numerator % i):
			maxi = i
	if maxi:
		s.add(numerator/maxi)
		s.add(denominator/maxi)
	return s
			
if __name__ == "__main__":
	product_numerator = 1
	product_denominator = 1
	for i in range(1,10):
		for j in range (i+1, 10):
			for i1 in range(1,10):
#				for i2 in range(1,10):
				if simplify(i*10+j, j*10 + i1) ==  simplify(i,i1):
					product_numerator *= i
					product_denominator *= i1
	print simplify(product_numerator, product_denominator)	
