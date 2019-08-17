#!/usr/bin/env python
import sys
from math import sqrt
from PIL import Image

if len(sys.argv) < 2:
	print("Prints average color (RGB) of input image")
	print("Usage: %s <input>" % sys.argv[0])
	exit(1)
inp = Image.open(sys.argv[1]).convert('RGBA')
ind = inp.load()
cl = ([], [], [])
for x in range(inp.size[0]):
	for y in range(inp.size[1]):
		px = ind[x, y]
		if px[3] < 128: continue # alpha
		cl[0].append(px[0]**2)
		cl[1].append(px[1]**2)
		cl[2].append(px[2]**2)

if len(cl[0]) == 0:
	file=sys.stderr
	print("Didn't find average color for %s %s" % sys.argv[1], file)
	print("0 0 0")
else:
	cl = tuple(sqrt(sum(x)/len(x)) for x in cl)
	print("%d %d %d" % cl)
