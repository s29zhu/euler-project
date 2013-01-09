#!include /usr/env/python


if __name__ == "__main__":
	for a in range(1,334):
		for b in range(a + 1,  500):
			if a**2 + b**2 == (1000 - a - b)**2:
				print a*b*(1000 - a - b)
