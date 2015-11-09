import csv
import sys

f = open(sys.argv[1], 'rt')

try:
	reader = csv.reader(f, quoting = csv.QUOTE_ALL)
	#for idx,row in enumerate(reader):
	#	if (idx == 0 or (idx%25) == 0):
			#s = str(row).strip('[').strip("]")
			#print s.replace("""'""","")
	#		print row
	for row in reader:
		print row
finally:
	f.close()
