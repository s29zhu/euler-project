#!include /usr/bin/python

import urllib2

if __name__ == "__main__":
	i = 1
	for i in range(1,401):
		content = urllib2.urlopen("http://projecteuler.net/problem="+str(i)).read()
		f = open(str(i)+".html", 'w+')
		f.write(content)
		f.close()
	#print content
	
