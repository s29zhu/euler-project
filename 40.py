#!include /usr/bin/python

if __name__ == "__main__":
	product = 1
	digit_num = 0
	j = 1
	i = 0
	while digit_num < 1000000:
		if j*9*10**(j-1) > 10**i:
			if j == 1:
				temp  = 1
			else:
				mx = int('9'*(j-1))
				temp = mx + (10**i - digit_num )/j + 1
			digit = int(str(temp)[(10**i - digit_num)%j-1])
			product *= digit
			print "22", digit, temp, j
			i += 1
		else:
			digit_num += j*9*10**(j-1)
			j += 1
	print product
