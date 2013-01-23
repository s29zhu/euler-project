#!include /usr/bin/python

from math import floor, sqrt

def isPrime(num):
	if num < 2:
		return False
	elif num == 2:
		return True
	else:
		for i in range(1, int(floor(sqrt(num)))+1):
			if (not num % i) and (not i == 1):
				return False
		return True

def primeSet(prime_num):
	prime_set = []
	prime_set.append(2)
	n = 1 
	while len(prime_set) < prime_num:
		if isPrime(n):
			prime_set.append(n)
		n += 2
	return prime_set			
	
if __name__ == "__main__":
	print	sorted(primeSet(20))
