#!include /usr/bin/python

from math import floor, sqrt

if __name__ == "__main__":
	count = 0
	f = open('words.txt','r+')
	l = eval(f.readline())
	for ele in l:
		value = 0
		for i in ele:
			value += ord(i) - ord('A') + 1
		sqr = int(floor(sqrt(value*2)))
		if sqr * (sqr+1) == value * 2:
			count += 1
	print count
