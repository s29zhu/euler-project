#!include /usr/env/python

from math import floor

def isPalindrome(testNum):
	#digits = []
	temp = 0
	original = testNum
	while(testNum):
		temp = testNum % 10 + temp * 10
		testNum = floor(testNum / 10)
	#digits.append(temp)
	#	print testNum, temp, original
	
	if temp == original:
		return True
	else: 
		return False

if __name__ == '__main__':
	maxpalindrome = 0
	for i in range(999, 100, -1) :
		for j in range(i, 100, -1):
			palindrome = i * j
			if(isPalindrome(palindrome)):
				if maxpalindrome < palindrome:
					maxpalindrome = palindrome
				
	print "palindrome", maxpalindrome
	
