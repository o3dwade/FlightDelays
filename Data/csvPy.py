import csv
import sys

f = open(sys.argv[1], 'rt')

try:
	#reader = csv.reader(f, quoting = csv.QUOTE_MINIMAL)
	#for idx,row in enumerate(reader):
	#	if (idx == 0 or (idx%20) == 0):
	#		#s = str(row).strip('[').strip("]").strip("""'""")
	#		print row
	for idx,line in enumerate(f):
		if (idx == 0 or (idx%50) == 0):
			print line
finally:
	f.close()
