import os
import json
import math
import random

data = []
for value in range(10):
	for other in range(10):
		x, y = random.random(), random.random()
		data.append((x,y))

print data	
