#!include /usr/bin/python

from math import factorial

if __name__ == "__main__":
	sum_i = 0
	summ = 0
	for i in range(3, 9999999):
		sum_i = 0
		string_i = str(i)
		for ele in string_i:
			sum_i += factorial(int(ele))
		if sum_i == i:
			summ += i
	print summ
