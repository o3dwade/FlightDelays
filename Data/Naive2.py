import csv
import sys
import random
import math
from collections import defaultdict

def getData(fileR,n):
	count=0
	reader = csv.reader(fileR)
	som = None
	for idx,row in enumerate(reader):
		count=count+1
		if (idx==0):
			som = row
		#print row
	C=count
	arr=[[0 for x in range(len(som))] for x in range(count)]
	f = open(sys.argv[n], 'r')
	reader = csv.reader(f)
	for idx,row in enumerate(reader):
		arr[idx] = row
		arr[idx]=str(arr[idx]).replace('[','').replace(']','')
		arr[idx]=str(arr[idx]).replace("\'",'')
		arr[idx]=str(arr[idx]).replace(" ",'')
	fileR.close()

	return arr

def probabilityOfLate(dataset):
	count = 0
	for row in dataset:
		if row[-1]=='1':
			count = count + 1
	return float(count)/float(len(dataset))

def lateInstances(dataset, opt):
	count = 0
	timeC = 0
	for row in dataset:
		if row[-1]=='1':
			count = count + 1
		if row[-1]=='0':
			timeC = timeC + 1
	if (opt=='late'):
		return float(count)
	else:
		return float(timeC)

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
	else:
		return time_set

def instanceProbabiltyCount(arr, inst):
	counts = defaultdict(lambda: 0)
	for i in range(len(arr)):
		cols = arr[i].split(',')
		for idx,c in enumerate(cols):
			if (idx==inst):
				#if c in counts:
				counts[c] +=  1
				#else:
				#	counts[c] = 1
	return counts


def main():
	
	f = open(sys.argv[1],'r')
	t = open(sys.argv[2],'rt')
	arr=getData(f,1)
	art=getData(t,2)
	late_prob = probabilityOfLate(arr)
	late_num = lateInstances(arr, 'late')
	time_num = lateInstances(arr, 'time')
	late_arr = delayedDataSet(arr,'late')
	ontime_arr=delayedDataSet(arr,'time')

	cols = arr[1].split(',')
	countDelay_arr=[]
	countOnTime_arr=[]
	for i in range(len(cols)):
		countDelay_arr.append(instanceProbabiltyCount(late_arr, i))
		countOnTime_arr.append(instanceProbabiltyCount(ontime_arr, i))
	#for key,value in count_arr[0].iteritems():
		#value = float(value)/float(late_num)
		#print key, value
	print "-------------------"
	TP=0
	TN=0
	FP=0
	FN=0
	for row in art:
		sumD=1
		sumT=1
		#for idx,col in enumerate(row.split(',')):
		#	sumD*=countDelay_arr[idx][col]/late_num
		#	sumT*=countOnTime_arr[idx][col]/time_num
		for i in range(len(cols)-1):
			sumD*=countDelay_arr[i][row.split(',')[i]]/late_num
			sumT*=countOnTime_arr[i][row.split(',')[i]]/time_num
		if (sumD>=sumT):
			if(row.split(',')[-1]=='1'):
				TN+=1
			else:
				FN+=1
		else:
			if(row.split(',')[-1]=='0'):
				TP+=1
			else:
				FP+=1
	print "Accuracy: " + str((float(TP+TN)/float(TP+TN+FP+FN))*100) +"%"

		

if __name__=="__main__":
	main()