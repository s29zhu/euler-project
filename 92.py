#!include /usr/bin/python

if __name__ == "__main__":
	count = 0
	s_89 = set()
	for i in range(1, 10000000):
		value = i
		while value != 89  and value != 1:
			i_str = str(value)
			value = 0
			for ch in i_str:
				value += int(ch)**2
			if value < i:
				if value in s_89:
					value = 89
				else:
					value = 1
				break 
		if value == 89:
			s_89.add(i)
			count += 1
	print count
