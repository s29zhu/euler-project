#!include /usr/bin/python

def symmetric(string):
	s = string
	while len(s) > 1:
		if s[0] == s[-1]:
			s = s[1:-1]
		else:	
			return False
	return True
	
if __name__ == "__main__":
	summ = 0
	for i in range(1,1000000,2):
		b_str = str(bin(i))[2:]
		i_str = str(i)
		if symmetric(i_str) and symmetric(b_str):
			summ += i
	print summ
