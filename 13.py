#!include /usr/bin/python

if __name__ == "__main__":
	
	l = 0 
	for row in open('13', 'r+'):
		l += long(row)
	print l	
