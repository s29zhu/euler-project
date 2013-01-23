#! usr/env/python

from math import sqrt, floor

def isPrime(num):
	for i in range(2, int(sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True

if __name__ == "__main__":
	prime_num = 0;
	diagnal_num = 0;

	#i represent the i-th layer
	for i in range(1, 20000):
		diagnal_num = 4 * i + 1
		up_right = (2 * i) ** 2 - 2 * i + 1
		if isPrime(up_right):
			prime_num += 1
		up_left = (2 * i) ** 2 + 1
		if isPrime(up_left):
			prime_num += 1
		down_left  = (2 * i) ** 2 + 2 * i + 1
		if isPrime(down_left):
			prime_num += 1
		if diagnal_num/prime_num >= 10:
			print 2 * i + 1
			break;
				
