import csv
import sys
import math
from collections import defaultdict

fileData = []

def getGain(arr):
	#readFile(fileName)

	ontime0 = 0
	delay1 = 0

	for line in fileData:
		#line = l.split(',')
		#if(line[0] == "AA"):
		if(line[len(line)-1] == "1"):
			delay1 += 1
		else:
			ontime0 += 1
	total = delay1 + ontime0
	originalEntropy = entropy(delay1, ontime0)

	gains = []
	for i in range(len(fileData[0])-1):
		if(fileData[0][i].isdigit()):
			time = True
		else: 
			time = False
		gains.append(calculateGain(i, originalEntropy, time))
		#print "attribute" , i , "with gain", (calculateGain(i, originalEntropy, time))
	return gains

def calculateGain(attr, originalEntropy, isNum):
	if(isNum):
		avg = average(attr)

		greaterDelay = 0
		lessDelay = 0
		greaterontime = 0
		lessonitme = 0

		for line in fileData:
			if(line[attr].isdigit()):
				if(int(line[attr]) > avg):
					if (line[len(line)-1] == "1"):
						greaterDelay += 1
					else:
						greaterontime +=1
				else:
					if (line[len(line)-1] == "1"):
						lessDelay += 1
					else:
						lessonitme += 1

						
		g = 0
		frac1 = (float(greaterontime + greaterDelay))/(len(fileData))
		g += frac1 * entropy(greaterDelay, greaterontime)
		frac2 = (float(lessonitme + lessDelay))/(len(fileData))
		g += frac2 * entropy(lessDelay, lessonitme)

		g = originalEntropy - g
		return g

	else:
		airlineEntropy = defaultdict(lambda: 0)
		for key,value in instanceDict(fileData, attr).iteritems():
			airlineEntropy[key] = calculateEntropy(attr, key)

		g = gain(airlineEntropy, originalEntropy, attr)
		return g


def gain(dictionary, originalEntropy, idx):
	total = len(fileData)
	gain = 0
	for key,value in instanceDict(fileData, idx).iteritems():
		gain += ((float(value)/float(total)) * (dictionary[key]))
		#print "gain", gain
	gain = originalEntropy - gain
	return gain

def instanceDict(arr, inst):
	counts = defaultdict(lambda: 0)
	for i in range(len(arr)):
		for idx,c in enumerate(arr[i]):
			if (idx==inst):
				counts[c] +=  1
	return counts



def calculateEntropy(attr, inst):
	delay1 = 0
	ontime0 = 0

	for line in fileData:
		if(line[attr] == inst):
			#print(line)
			if(line[len(line)-1] == "1"):
				delay1 += 1
			else:
				ontime0 += 1
	#print "delay", delay1, "ontime", ontime0
	entr = entropy(delay1, ontime0)
	return entr



	
def entropy(delay, ontime):
	total = delay + ontime
	delayFrac = float(delay)/float(total)
	ontimeFrac = float(ontime)/float(total)

	if(delayFrac == 0 or ontimeFrac == 0):
		return 0
	else:
		en = -(float((float(delay)/float(total)) * math.log((float(delay)/float(total)), 2))) - float((float(ontime)/float(total)) * math.log((float(ontime)/float(total)), 2))
		return en

def readFile(name): 
	ofile = open(name)
	reader = csv.reader(ofile)

	for line in reader:
		if line != []: 
			#print(line)
			fileData.append(line)

	ofile.close()

def average(attr):
	avg = 0
	for line in fileData:
		if(line[attr].isdigit()):
			avg += int(line[attr])


	avg = avg / len(fileData)
	return avg 



if __name__ == "__main__": getGain()
