#! usr/env/python

from math import sqrt, floor

def isPrime(num, primeList):
	for i in primeList:
		if i > sqrt(num):
			primeList.append(num)
			return True
		elif num % i == 0:
			return False

if __name__ == "__main__":
	primeList = [2]
	sumPrime = 2
	for i in range(3, 2000000):
		if isPrime(i, primeList):
			sumPrime += i
	print sumPrime


			
