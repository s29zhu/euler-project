#!include /usr/bin/python

from math import floor, sqrt

def prime(num):
	for i in range(1, int(floor(sqrt(num)))+1):
		if not num % i and not i == 1:
			return False
	return True	
def circuPrime(num):
	temp_num = num
	num = num[-1] + num[:-1]
	while not temp_num == num:
		if not prime(int(num)):
			return False
		num = num[-1] + num[:-1]
	return True

if __name__ == "__main__":
	count = 0 
	for i in range (2, 1000000):
		if prime(i):
			string_i = str(i)
			if circuPrime(string_i):
				print i
				count += 1
	print count
