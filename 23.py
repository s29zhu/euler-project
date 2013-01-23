#!include /usr/bin/python

from math import floor, sqrt

def divisorSum(num):
	d = []
	i = 0
	if num == 0 or num == 1:
		return 0;
	for  i in range(1, int(floor(sqrt(num))) + 1):
		if not num % i:
			d.append(i)
			if num / i != i:
				d.append(num / i)
	if num in d:
		d.remove(num)
	#print d, num
	return sum(d)

if __name__ == "__main__":
	abu = []
	summ = []
	f = False
	for i in range(1, 28123):
		f = False
		if divisorSum(i) > i:
			abu.append(i)
		for j in abu:
#			print j 
			if i - j in abu:
				f = True
				break
		if not f:
			summ.append(i)
#	print summ
	print long(sum(summ))
	print 28123*28122/2 - long(sum(summ))
