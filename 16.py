#!include /usr/env/python

from math import factorial

if __name__ == '__main__':
	
	a = pow(2,1000)
	b = str(a)
	length = len(b)
	i = 0
	temp = 0

	while(i < length):
		temp += int(b[i])
		i = i + 1
	print " The sum is ", temp		
