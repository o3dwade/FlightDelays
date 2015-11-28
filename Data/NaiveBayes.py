import csv
import sys
import random
import math

arr = None

def main():
	counts = {}
	initialize()
	cols = arr[1].split(',')
	for i in range(len(cols)):
		if (i==0):
			print cols[i]
	for i in range(len(arr)):
		cols = arr[i].split(',')
		for idx,c in enumerate(cols):
			if c in counts:
				counts[c] = counts[c] + 1
			else:
				counts[c] = 1
	


def initialize():
	global arr
	count=0
	f = open(sys.argv[1],'rt')
	reader = csv.reader(f)
	som = None
	for idx,row in enumerate(reader):
		count=count+1
		if (idx==1):
			som = row
		#print row
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

		#print arr[idx]



		#print arr[i]


if __name__=="__main__":
	main()