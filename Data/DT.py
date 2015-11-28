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
	arr=[[0 for x in range(len(som))] for x in range(count)]
	f = open(sys.argv[n], 'r')
	reader = csv.reader(f)
	for idx,row in enumerate(reader):
		arr[idx] = row
		arr[idx]=str(arr[idx]).replace('[','').replace(']','')
		arr[idx]=str(arr[idx]).replace("\'",'')
		arr[idx]=str(arr[idx]).replace(" ",'')
		#print arr[idx]
	fileR.close()
	return arr


def classInstancesCount(dataset, opt):
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

def classDataSet(dataset, opt):
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

def instanceDict(arr, inst):
	counts = defaultdict(lambda: 0)
	for i in range(len(arr)):
		cols = arr[i].split(',')
		for idx,c in enumerate(cols):
			if (idx==inst):
				counts[c] +=  1
	return counts

def main():
	f = open(sys.argv[1],'r')
	t = open(sys.argv[2],'rt')
	arr=getData(f,1)
	art=getData(t,2)
	late_num = classInstancesCount(arr, 'late')
	time_num = classInstancesCount(arr, 'time')
	late_arr = classDataSet(arr,'late')
	ontime_arr=classDataSet(arr,'time')

	cols = arr[1].split(',')
	delay_dict_arr=[]
	time_dict_arr=[]
	all_Dict_arr=[]
	for i in range(len(cols)):
		delay_dict_arr.append(instanceDict(late_arr, i))
		time_dict_arr.append(instanceDict(ontime_arr, i))
		all_Dict_arr.append(instanceDict(arr, i))
	for key,value in delay_dict_arr[0].iteritems():
		print key, value

	TP=0
	TN=0
	FP=0
	FN=0
	for row in art:
		for idx in range(len(cols)-1):
			val=row.split(',')[idx]
			#prob_all+=countAll[idx][val]
			#if (idx==0):
				#print str(val)+" "+str(countAll[idx][val])

		if (2>=0):
			if(row.split(',')[-1]=='1'):
				TN+=1
			else:
				FN+=1
		else:
			if(row.split(',')[-1]=='0'):
				TP+=1
			else:
				FP+=1

	print "----- Confusion Matrix -----\n a    b      classified as\n "+str(TP)+" "+str(FN)+""+" |    a = 0\n "+str(FP)+" "+str(TN)+""+" |    b = 1"


	print "Accuracy: " + str(round((float(TP+TN)/float(TP+TN+FP+FN))*100,2)) +"%"

if __name__=="__main__":
	main()