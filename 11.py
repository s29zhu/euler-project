#!include /usr/env/python

if __name__ == "__main__":
	
	grid = []
	for line in open('./11','r'):
		line = line[0:-1]
		grid.append(line.split(" "))
	#print grid
	term = ''
	maxm = 0
	for row in grid:	
		for item in row:
			i = grid.index(row)
			j = row.index(item)
		#	maxm = 0
			temp = 1
#			h = row[j:j + 4]
			for h in range(j, j + 4):
				if h >= 20:
					break
				temp *= int(grid[i][h])
			if temp > maxm:
				maxm = temp
				term = 'h'+grid[i][j]
			temp = 1
			for k in range(i, i + 4):
				if(k >= 20):
					break
				temp *= int(grid[k][j])
			if temp > maxm:
				maxm = temp
				term = 'v'+grid[i][j]
			temp = 1
			for k in range(0, 4):
				if j + 4 >= 20 or i + 4 >= 20:
					break
				temp *= int(grid[i+k][j+k])
			if temp > maxm:
				maxm = temp
				term = 'dr'+grid[i][j]
			temp = 1
			for k in range(0, 4):
				if i + 4 >= 20 or j - 4 < 0:
					break
				temp *= int(grid[i+k][j-k])
			if temp > maxm:
				maxm = temp
				term = 'dl'+grid[i][j]
	print maxm, term	
		
