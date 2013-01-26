#! include /usr/bin/python

from prime import isPrime
from itertools import *
					
if __name__ == "__main__":
	b = 1000
	found = False
	lis_type = []
	while b < 10000:
		if isPrime(b):
			lis_type.append(sorted(str(b)))
		b += 1
	for ele in lis_type:
		li = set()
		a = permutations(ele)
		for b in a:
			temp = 0
			for c in b:
				temp = temp*10 +int(c)
			if isPrime(temp) and len(str(temp)) == 4:
				li.add(temp)
		if len(li) < 3:
			continue
		c = permutations(li, 3)
		for d in c:
			d = sorted(d)
			if d[2] + d[0] == 2*d[1] and d[0] != 1487 :
				print d[0], d[1], d[2]
				found = True
				break
		if found:
			break
		del(li)
