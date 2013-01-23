#!include /usr/bin/python

if __name__ == "__main__":
	f = open("22names.txt","r+")
	string = f.read().strip('''"''')
	l = string.split('''","''')
	l = sorted(l)	
	f.close()
	summ = 0
	for ele in l:
		value = 0
		for i in ele:
			value += ord(i) - 64
		summ += value * (l.index(ele)+1)
	print summ
