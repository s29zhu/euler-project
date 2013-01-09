#!include /usr/bin/python

if __name__ == "__main__":
	j = 1
	i = 1
	num = i + j
	count = 3
	while num < 10**999:
		j = i + num
		i = j + num
		num = i + j
		count += 3 
	if j >= 10 ** 999:
		print count - 2
	elif i >= 10 ** 999:
		print count - 1
	else:
		print count
	
