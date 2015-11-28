import csv
import sys
import random
import math

k = sys.argv[2]
arr = None

def main():
	initialize()
	print arr[0].split(',')
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

	for i in range(len(arr)):
		arr[i]=str(arr[i]).replace('[','').replace(']','')
		arr[i]=str(arr[i]).replace("\'",'')
		#print arr[i]


if __name__=="__main__":
	main()