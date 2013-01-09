#!include /usr/bin/python

if __name__ == "__main__":
	f = open("triangle.txt", 'r+')
	triangle = []
	pre = []
	for line in f:
		line = line[:-1]
		temp = line.split(' ')
		triangle.append(temp)
		
	triangle.reverse()
	print triangle	
	for l in triangle:
		if(len(pre) == 0):
			pre = l
			continue
		else:
			for ele in l:
				if pre[l.index(ele)] >= pre[l.index(ele)+1]:
					l[l.index(ele)] = int(l[l.index(ele)]) + int(pre[l.index(ele)])
			 	else:
					l[l.index(ele)] = int(l[l.index(ele)]) + int(pre[l.index(ele)+1])
			triangle[triangle.index(l)] = l
			pre = l
	print triangle
				
					
		
