#!include /usr/bin/python

from math import sqrt, floor

def isPrime(num):
	if num < 2:
		return False
	for i in range(1,int(floor(sqrt(num))) + 1):
		if not num % i and i != 1:
			return False
	return True

if __name__ == "__main__":
	prime = []
	for i in range(1000000):
		if isPrime(i):
			prime.append(i)
	prime = sorted(prime)
	print len(prime)
	for j in range(500, 550):
		i = 0
		summ = sum(prime[i: i + j])
		while i + j < len(prime) and summ <= prime[-1]:
			if summ in prime[i + j:]:
				print "find one", i, j, summ
				break
			else:
				if i + j < len(prime):
					summ = summ - prime[i] + prime[i + j]
				i += 1
