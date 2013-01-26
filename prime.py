#!include /usr/bin/python

from math import floor, sqrt

# isPrime function returns whether or not the given number is prime
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

# Given a prime_num, primeList returns the first prime_num numbers
def primeList(prime_num):
	prime_list = []
	prime_list.append(2)
	n = 1 
	while len(prime_list) < prime_num:
		if isPrime(n):
			prime_list.append(n)
		n += 2
	return prime_list			

# primeFactorsOfNum function returns the prime factors set of given number 
def primeFactorsOfNum(num, prime_list):
	factors = set()
	if isPrime(num):
		factors.add(num)
		return factors
#	prime_list = primeList(num/2)
	for ele in prime_list:
		if ele > num:
			break
		while not num % ele:
			factors.add(ele)
			num /= ele	
	return factors

if __name__ == "__main__":
	print	sorted(primeSet(20))
