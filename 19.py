#!include /usr/bin/python

if __name__ == "__main__":
	
	year = [31,29,31,30,31,30,31,31,30,31,30,31]
	year = 1900
	count = 0
	total = 0

	while(year < 2001):
		if not year % 400:
			year[1] = 29
		elif not year % 100:
			year[1] = 28
		elif not year % 4:
			year[1] = 29
		else:
			year[1] = 28

		for item in year:
			total += item
			if not (total + 1) % 7:
				count += 1
		if year == 1900:
			pre = count
		year += 1
	print count-pre
	
	
