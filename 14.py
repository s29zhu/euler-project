#!include /usr/bin/python

if __name__ == "__main__":
	
	item = 1
	counter = 0
	temp = 0
	maxm = 0
	mnum = 0
	while(item < 1000000):
		counter = 0
		temp = item
		while(temp != 1):
			counter += 1
			if temp % 2:
				temp = 3 * temp + 1
			else:
				temp /= 2
		if counter > maxm:
			maxm = counter
			mnum = item
		item += 1
	print mnum, maxm
