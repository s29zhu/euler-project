#!include /usr/bin/python

def compose(l, total, ele):
	count = 0
	if ele <= total:
		if ele == 1 or ele == total:
			count += 1
		else:
			for i in l[:l.index(ele)+1]:
				count += compose(l, total-ele, i)
	return count		

if __name__ == "__main__":
	l = [1,2,5,10,20,50,100,200]
	count = 0
	for ele in l:
		count += compose(l,200,ele)
	print count
