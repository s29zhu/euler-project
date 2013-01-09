#!include /usr/bin/python

if __name__ == "__main__":
	string = '9'
	summ = 0
	i = 2
#upper bound int(string), all the numbers that satisfied shouldn't be beyong 
#this range
	temp = sum(int(i)**5 for i in string)
	while temp > int(string):
		string += '9'
		temp = sum(int(i)**5 for i in string)
	while i < int(string):
		temp = sum(int(di)**5 for di in str(i))
		if temp == i:
			summ += i
		i += 1
	print summ
