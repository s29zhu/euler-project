#!include /usr/bin/python

import math

def LCM(a, b):
	gcd = 1
	if a <= b:
		sqroot = a
	else:
		sqroot = b
	for i in range(sqroot, 1, -1):
		if((not a % i) and (not b % i)): 
			gcd = i
			break 
	lcm = a * b / gcd
	return lcm

if __name__ == '__main__':
	lcm = 1 
	for i in range(1, 21):
		lcm = LCM(i, lcm)
	print "lcm is ", lcm
