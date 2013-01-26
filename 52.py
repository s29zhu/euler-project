#!include /usr/bin/python

if __name__ == "__main__":
	
	for i in range(125875, 1000000):
		set_i = set(str(i))
		origin_set = set_i
		set_i = set_i.union(set(str(2*i)).union(set(str(3*i)).union(set(str(4*i)).union(set(str(5*i)).union(set(str(6*i)))))))
		if origin_set == set_i:
			print i
			break
