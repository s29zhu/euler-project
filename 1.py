#!include /usr/bin/python

import math
if __name__ == '__main__':
	threeSum = 0
	fiveSum = 0
	fifteenSum = 0 
	summ = 0
	threeSum = 3*math.floor(1000/3)*(math.floor(1000/3)+1)/2
	fiveSum = 5*math.floor(999/5)*(math.floor(999/5)+1)/2
	fifteenSum = 15*math.floor(1000/15)*(math.floor(1000/15)+1)/2
	summ = threeSum + fiveSum - fifteenSum
	print threeSum, fiveSum, fifteenSum, summ
	
