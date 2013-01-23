#!include /usr/bin/pyt

from  PrimeGenerate import primeSet, isPrime
from math import floor, sqrt
	
if __name__ == "__main__":
	j = 1
	n = 33
	flag = True
	prime_set = primeSet(1500)
	sorted(prime_set)
	while flag:
		n += 2
		if isPrime(n):
			continue
		flag = False
		for ele in prime_set:
			if ele >= n:
				break
			if  (n - ele)%2:
				continue
			temp = (n - ele)/2
			if temp == int(floor(sqrt(temp)))**2:
				flag = True
				break
	print n
