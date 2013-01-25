#!include /usr/bin/python

def perm(string, n = None):
	if n is None:
		n = len(string)
	for i in range(len(string)):
		v = string[i]
		if n == 1:
			yield v
		else:
			sub_string = string[:i] + string[i+1:]
			for p in perm(sub_string, n - 1):
				yield v + p

if __name__ == "__main__":
	s = '0123456789'
	l = [2,3,5,7,11,13,17]
	summ = 0 
	result = perm(s)
	for ele in result:
		flag = 0
		for i in range(1, 8):
			if int(ele[i:i+3]) % l[i-1]:
				break
			else :
				flag += 1
		if flag == 7:
			summ += int(ele)
	print summ
