import csv
import sys

f = open(sys.argv[1], 'rt')

try:
	for idx,line in enumerate(f):
		if (idx == 0 or (idx%50) == 0):
			print line
finally:
	f.close()
