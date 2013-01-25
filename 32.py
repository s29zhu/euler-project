#!include /usr/bin/python
#only 1 digit * 4 digits = 4 digits
#or 2 digits * 3 digits = 4 digits
def permutate(l, st, s):
	l1 = ''
	if l == '':
		if int(st[:1]) * int(st[1:5]) == int(st[5:]):
			s.add(int(st[5:]))
		if int(st[:2]) * int(st[2:5]) == int(st[5:]):
			s.add(int(st[5:]))
	else:
		for ele in l:
			st += ele
			l1 = l.replace(ele,'')
			permutate(l1, st, s)
			st = st.replace(ele, '')		

if __name__ == "__main__":
	s = set('')
	l = '123456789'
	st = ''
	permutate(l, st, s)
	print sum(s)
