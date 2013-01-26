#!include /usr/bin/python

from math import factorial

if __name__ == "__main__":	
	total = 0
	for n in range(1, 100 + 1):
		fact_n = factorial(n)
		for r  in range(1, n/2 + 1):
			combin = (fact_n/factorial(r))/factorial(n-r)
			if combin > 1000000 :
				total += n + 1 - 2 * r
				break
	print total
