#!include /usr/bin/python

if __name__ == "__main__":
	i = 1
	max_length = 0
	m = 0
	while i < 1000:
		l = []
		numerator = 1
		while not numerator in l:
			l.append(numerator)
			while numerator < i:
				numerator *= 10
			if numerator % i: 
				numerator = numerator % i
			else:
				break 
		if (numerator in l) and (len(l) - l.index(numerator) > max_length):
			m = i
			max_length = len(l) - l.index(numerator) 
		del l[:]
		i += 1
	print max_length, m
