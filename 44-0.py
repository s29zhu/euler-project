#!include /usr/bin/python

from math import floor, sqrt

if __name__ == "__main__":
	l = [1]
	n = 2
	flag = True
	res = 0
	lis = []
	for i in range(2500):
		lis.append((3*i**2-i)/2)
	while flag:
		p1 = n*(3*n-1)/2
		for p0 in l:
			if p1+p0 in lis and p1-p0 in lis:
				res = p1-p0
				flag = False
				break
		l.append(p1)
		n += 1
	print res
