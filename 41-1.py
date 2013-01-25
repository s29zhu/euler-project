#!include /usr/bin/python

from math import floor, sqrt
def prime(num):
        if num < 2:
                return False
        elif num == 2:
                return True
        else:
                for i in range(1, int(floor(sqrt(num)))):
                        if num % i == 0 and not i == 1:
                                return False
                return True

if __name__ == "__main__":
	maxi = 0
	i = 9999999
	while i > 0:
		candidate_set = sorted(set(str(i)))
		if (not '0' in candidate_set) and (candidate_set[-1] == str(len(candidate_set))):
			print i
			if prime(i) and maxi < i:
				maxi = i
				break
		i -= 1
	print maxi	
