#!include /usr/bin/python

if __name__ == "__main__":
	s = set()
	for a in range(2,101):
		for b in range(2,101):
			s.add(a**b)
	print len(s)
