#! include /usr/bin/python

def sumDigi(num):
	summ = 0
	digi_set = list(str(num))
	for ele in digi_set:
		summ += int(ele)
	return summ
	
if __name__ == "__main__":
	maxm = 0
	for a in range(1,100):
		for b in range(1, 100):
			summ = sumDigi(a**b)
			if sumDigi(a**b) > maxm:
				maxm = summ
	print maxm
