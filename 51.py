#!include /usr/bin/python

from math import sqrt, floor
from itertools import *

def isPrime(num):
	if num < 2:
		return False
	for i in range(1, int(floor(sqrt(num))) + 1):
		if not num % i and i != 1:
			return False
	return True
# This function returns the digits' index(es)	
def pattern(num):
	index = {}
	i = 0
	for ch in num:
		if not ch in index.keys():
			index[ch] = []	
			index[ch].append(i)
		else:
			index[ch].append(i)
		i += 1
	return index

if __name__ == "__main__":
	candi = 100000
	primes = []
	prime_set = []
	l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	flag = False
	for candi in range(100000, 1000000):
		if isPrime(candi) and candi % 10 == 3:
			primes.append(candi)
	for ele in primes:
		ele_str = str(ele)
		patt_dic = pattern(ele_str[:-1])
		for i in patt_dic:# for every digit in the prime number
			j = patt_dic[i]# get the index(es) of the digit
			length = len(j)
			for k in range(1, length + 1):
				list_temp = combinations(j, k)# replace some of the digits				
				for y in list_temp:
					prime_set = []
					if 0 in y:
						l = l2
					else: 
						l = l1
					for item in l:
						string = ele_str
						for it in y:
							string = string[: it] + str(item) + string[it + 1:]
						if isPrime(int(string)):
							prime_set.append(int(string))
					if len(prime_set) == 8:
						prime_set = sorted(prime_set)
						print prime_set
						flag = True
						break
		if flag:
			break
