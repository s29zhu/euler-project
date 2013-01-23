#!include /usr/bin/python

from math import floor, ceil, sqrt, fabs

def prime(num):
	num = fabs(num)
	i = 2
	while i <= floor(sqrt(num)):
		if not num%i:
			return False
		i += 1
	return True
	
def quatraticPoly(a,b,n):
	res= n**2 + a*n + b
	if prime(res):
		return True
	else:
		return False

if __name__ == "__main__":
	n = 0
	maxi = 0
	product = 0
##a must be odd, and b must be prime
	for a in range(-999, 1000, 2):
		for b in range(-999, 1000, 2):
			n = 0
			while quatraticPoly(a,b,n):
				 n += 1		
			if maxi < n:
				maxi = n + 1  
				product = a * b
	print product
