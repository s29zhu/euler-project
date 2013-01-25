#!include /usr/bin/python

if __name__ == "__main__":
	
	length = 0
	maxi = ''
	for i in range(1, 10000):
		string = ''
		j = 1
		while len(string) < 9:
			string += str(i*j)
			j += 1
		if len(string) == 9 and not '0' in string:
			s = set(string)
			if len(s) == 9 and maxi < string:
				maxi = string
	print maxi	
 
