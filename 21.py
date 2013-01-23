#!include /usr/bin/python

from math import floor, sqrt

def divisorSum(num):
	d = []
	i = 0
	if num == 0 or num == 1:
		return 0
	for i in range(1, int(floor(sqrt(num)))+1):
		if not (num % i):
			d.append(i)
			if num/i != i:
				d.append(num / i)	
	if num in d:
		d.remove(num)	
	return sum(d)

if __name__ == "__main__":
	l = []
	for i in range(1, 10000):
		if not i in l:
			temp = divisorSum(i)
			if divisorSum(temp) == i and temp != i:
				l.append(temp)
				l.append(i)
	print sum(l)
						
