#!include /usr/bin/python

from math import factorial

if __name__ == "__main__":
	nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	total = 1000000
	seq = 0
	for i in range(9,0,-1):
		quot = int(total/factorial(i))
		if quot:
			seq = seq*10 + nums[quot]
			total -= quot*factorial(i)
			nums.pop(quot)
		else:
			nums.append(seq%10)
			nums.sort()
			ele = nums.pop(nums.index(seq%10)-1)
			seq = seq - seq%10 + ele
			nums.reverse()
			for ele in nums:
				seq = seq*10 + ele
	print seq
