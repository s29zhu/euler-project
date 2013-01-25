#!include  /usr/bin/python

from math import floor, sqrt

if __name__ == "__main__":
	maxi = 0
	for i in range(12, 1000):
		count = 0
		c = i / 3 + 1
		for c in range(c, i - 1):
			for a in range(1, (i - c)/2):
				b = i - a - c
				if b**2 + a**2 == c**2:		
					count += 1
		if maxi < count:
			maxi = count
			max_p = i
	print maxi, max_p
