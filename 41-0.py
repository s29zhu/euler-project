#! include /usr/bin/python

from math import floor, sqrt
def prime(num):
        if num < 2:
                return False
        elif num == 2:
                return True
        else:
                for i in range(1, int(floor(sqrt(num)))):
                        if num % i == 0 and not i == 1:
                                return False
                return True

def perm(items, n=None):
    if n is None:
        n = len(items)
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1:
            yield v
        else:
            rest = items[:i] + items[i+1:]
            for p in perm(rest, n-1):
                yield v + p

if __name__ == "__main__":
	string = '7654321'
	maxi = ''
	for i in range(7, 1, -1):
		a = perm(string)
		for b in a:
			if prime(int(b)):
				print b
				maxi = b
				break
		if not maxi == '':
			break
