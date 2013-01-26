#! include /usr/bin/python

from math import *
from itertools import *
from string import *

if __name__ == "__main__":
	f = open("cipher1.txt", "r+")
	cipher = eval(f.read())
	cipher_length = len(cipher)
	key_range = range(97, 123)
	#most common words, see wikipedia
	common_words = ['the','be','to','of','and','a','in',\
		'that','have']
	keys = product(key_range, repeat = 3)
	for k in keys:
		plain_text = ''
		key = k * (cipher_length / 3) +  k[:cipher_length % 3]
	#	print len(key), cipher_length
		for i in range(cipher_length):
			plain = cipher[i] ^ key[i]
			plain_text += chr(plain)
		for item in common_words:
			if not item in plain_text:
				break
		if item == 'have':
			print "Found", k , plain_text
			print sum(ord(item) for item in plain_text)
			break		
			
