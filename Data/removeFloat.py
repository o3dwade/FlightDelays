import csv
import sys
import random
import math



def main():
	
	f = open(sys.argv[1],'rt')
	count=0
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
	arr.remove(arr[0])

	for i in range(len(arr)):
		for idx,col in enumerate(arr[i].split(',')):
			if (len(col)>4):
				val=str(int(float(arr[i].split(',')[idx])))
				arr[i] =  arr[i].replace(col,val)
				#print arr[i].replace(col,val)
	for row in arr:
		print row
	#for key,value in instanceProbabiltyCount(arr, 2).iteritems():
		#print key, value

if __name__=="__main__":
	main()