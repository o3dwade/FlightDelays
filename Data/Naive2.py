import csv
import sys
import random
import math


def getData(fileR):
	count=0
	reader = csv.reader(fileR)
	som = None
	for idx,row in enumerate(reader):
		count=count+1
		if (idx==1):
			som = row
		print row
	C=count
	points = [0 for x in range(int(C))]
	arr=[[0 for x in range(len(som))] for x in range(count)]
	global pt
	pt = [[0 for x in range(len(som))] for x in range(count)]
	f = open(sys.argv[1], 'r')
	reader = csv.reader(f)
	for idx,row in enumerate(reader):
		arr[idx] = row
		arr[idx]=str(arr[idx]).replace('[','').replace(']','')
		arr[idx]=str(arr[idx]).replace("\'",'')
		arr[idx]=str(arr[idx]).replace(" ",'')
	arr.remove(arr[0])

	return arr

def probabilityOfLate(dataset):
	count = 0
	for row in dataset:
		if row[-1]=='1':
			count = count + 1
	return float(count)/float(len(dataset))

def delayedDataSet(dataset, opt):
	late_set = []
	time_set = []
	for row in dataset:
		if (row[-1] == '1'):
			late_set.append(row)
		else:
			time_set.append(row)
	if (opt == 'late'):
		return late_set
	elif (opt =='time'):
		return time_set
	else:
		return "Error you need to enter either \"late\" or \"time\""

def instanceProbabiltyCount(arr, inst):
	counts = {}
	for i in range(len(arr)):
		cols = arr[i].split(',')
		for idx,c in enumerate(cols):
			if (idx==inst):
				if c in counts:
					counts[c] = counts[c] + 1
				else:
					counts[c] = 1
	return counts


def main():
	
	f = open(sys.argv[1],'rt')
	arr=getData(f)
	late_prob = probabilityOfLate(arr)
	late_flights = delayedDataSet(arr,'late')
	ontime_flights=delayedDataSet(arr,'time')

	cols = arr[1].split(',')

	#for key,value in instanceProbabiltyCount(arr, 2).iteritems():
		#print key, value

if __name__=="__main__":
	main()