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
	sum1 = []
	sum2 = []
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
			sum1.append(i)
		else:
			sum2.append(i)
	set1 = set(sum1)
	set2 = set(sum2)
	sets = set(range(1, 28123))
	print sets - set1|set2 
#	print summ
	print long(sum(summ))
	print (len(abu)+1)*long(sum(abu))
