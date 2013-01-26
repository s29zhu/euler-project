#! incldue /usr/bin/python

def reverseNum(num):
	reverse = 0
	while num >= 10:
		reverse = reverse*10 + num % 10
		num = num/10
	reverse = reverse*10 + num % 10
	return reverse		

if __name__ == "__main__":
	num = 0
	for candi in range(1, 10000):
		temp = candi
		for iteration in range(1, 51):
			candi = candi + reverseNum(candi)
			if reverseNum(candi) == candi:
				break
		if iteration == 50:
			num += 1
	print num 					
			
