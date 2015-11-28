import csv
import sys
import math

fileData = []

def main():
	readFile(sys.argv[1])

	ontime0 = 0
	delay1 = 0

	print(len(fileData))
	for line in fileData:
		#if(line[0] == "AA"):
		if(line[4] == "1"):
			delay1 += 1
		else:
			ontime0 += 1
	total = delay1 + ontime0
	print "AA dalayed" , delay1, "on time", ontime0, "total", delay1+ontime0
	entropy = -(float((float(delay1)/float(total)) * math.log((float(delay1)/float(total)), 2))) - float((float(ontime0)/float(total)) * math.log((float(ontime0)/float(total)), 2))
	print "entropy", entropy

def readFile(name): 
	ofile = open(name)
	reader = csv.reader(ofile)

	for line in reader:
		if line != []: 
			#print(line)
			fileData.append(line)

	ofile.close()






if __name__ == "__main__": main()
