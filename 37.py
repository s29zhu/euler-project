#!include /usr/bin/python

from math import floor, sqrt

def prime(num):
    for i in range(1, int(floor(sqrt(num)))+1):
        if not num % i and not i == 1: 
            return False
	if num == 1:
		return False
    return True

def truncPrime(num):
	num_str = str(num)
	for i in range(0, len(num_str)):
		temp_num1 = int(num_str[i:])
		temp_num2 = int(num_str[:len(num_str)-i])
		if not prime(temp_num1) or not prime(temp_num2):
			return False
	return True
	
if __name__ == "__main__":
	count = 11
	candidate = 11
	summ = 0
	while count > 0:
		if truncPrime(candidate):
			count -= 1
			summ += candidate
		candidate += 2
	print summ
