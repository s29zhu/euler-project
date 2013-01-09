#! include /usr/bin/python

from math import *

if __name__ == "__main__":
	f = open('base_exp.txt', 'r+')
	l = eval(f.readline())
	max_value = 0.0
	max_line = 0
	i = 1
	while len(l) == 2:
		value = l[1] * log(l[0], 2) # both log1p and log10 yields to smaller values 
									# that are difficult to distinguish
		print l,float(l[1]),log1p(float(l[0])), value, max_value	
		if value > max_value:
			max_value = value
			max_line = i
		temp = f.readline()
		if temp:
			l = eval(temp)
		else:
			 l = []
		i += 1
	print max_line
