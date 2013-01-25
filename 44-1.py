#!/usr/bin/env pypy
# 1560090 7042750 8602840
pant_numb = set()
for i in range(1, 2500):
    pant_numb.add(i * (3 * i - 1) / 2)

set_d = set()
for x in pant_numb:
    for y in pant_numb:
        if x == y:
            continue

        if x + y in pant_numb and abs(x - y) in pant_numb:
			print x, y	
			set_d.add(abs(x - y))
print set_d
print min(set_d)
