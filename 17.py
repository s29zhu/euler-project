#!include /usr/env/python

from sets import Set

if __name__ == '__main__':
	
	letterList = Set([])
	unit = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine']
	teen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
		      'sixteen', 'seventeen', 'eighteen', 'nineteen'] 
	decade = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	hundred = 'hundred'
	thousand = 'thousand'
	temp = 0
	lHandred = 0
	for a in unit:
		temp += len(a)
	print temp
	for a in teen:
		temp += len(a)
	print temp
	for a in decade:
		temp += len(a)
	print temp
	for a in decade:
		for b in unit:
			temp += len(a) + len(b)
	print temp
	lHandred = temp
	
	for a in unit:
		temp += lHandred + 99 * (len(a) + len(hundred) + len('and'))	
		print a, temp
	temp += len('one') + len('thousand')
	for a in unit:
		temp += len(a) + len('hundred')
	print temp
