#! include /usr/bin/python

from prime import isPrime
from itertools import *
					
if __name__ == "__main__":
	digits = '123456789'
	a = permutations(digits, 4)
	lis_type = []
	l = []
	for b in a:
		temp = 0
		for digit in b:
			temp = temp*10 + int(digit)
		if isPrime(temp):
			l.append(temp)
	c = permutations(l,3)
	for d in c:
		d = sorted(d)
		if sorted(str(d[0])) == sorted(str(d[1])) and sorted(str(d[1])) == sorted(str(d[2])):
			if d[0] + d[2] == 2*d[1] and d[0] != 1487:
				print d[0], d[1], d[2]
				#break
	
