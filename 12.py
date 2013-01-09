#!include  /usr/bin/python 

from math import sqrt, floor


def divide(num, divisor):
	item = 1
	sqr = floor(sqrt(num))
	while(item < sqr):
		if not num % item:
			divisor.append(item)
			divisor.append(num/item)
		item += 1
	return divisor	
	
if __name__ == "__main__":
	n = 1
	length = 0
	while(length < 500):
		divisor = []
		divisor = divide(n*(n+1)/2,divisor)
		length = len(divisor)
		n += 1
	print  n-1, n*(n-1)/2
	
