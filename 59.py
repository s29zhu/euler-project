#! include /usr/bin/python

from math import *
from itertools import *
from string import *

if __name__ == "__main__":
	f = open("cipher1.txt", "r+")
	cipher = eval(f.read())
	key_range = range(97, 123)
	key = permutations(key_range, 3)
	for k in key:
		print join(chr(i) for i in k)		
