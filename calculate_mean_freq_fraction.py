##!/usr/bin/env python3.5
import csv
import os
import re
import sys
from difflib import ndiff
from difflib import SequenceMatcher
import numpy as np
from numpy import zeros
from statsmodels.stats.proportion import proportions_ztest


#script to check for presence and count a set of barcodes in a file
#
#usage: calculate_enrichment*.py countfile  countfile2

#outdir = sys.argv[1]

countfile = sys.argv[1]
countfile2 = sys.argv[2]
countfile3 = sys.argv[3]
countfile4 = sys.argv[4]
countfile5 = sys.argv[5]

cont=0
#cont2=0

count_dict = dict([])
seq_dict= dict([])


nreads=0
nreads2=0
nreads3=0
nreads4=0
nreads5=0

with open(countfile,'r') as f:
	for line in f:
		#reader=csv.reader(line,delimiter='\t')
		line1=line.split("\t")
		seq=line1[1]
		count=line1[0]
		nreads=nreads+float(count)
		seq=seq.strip('\n')
		if not seq in count_dict:
			count_dict[seq]=zeros([1,5])
#		print(str(count_dict[seq]))
		count_dict[seq][0]=float(count)

with open(countfile2,'r') as f:
	for line in f:
		line1=line.split("\t")
		seq=line1[1]
		count=line1[0]
		nreads2=nreads2+float(count)
		seq=seq.strip('\n')
		if not seq in count_dict:
			count_dict[seq]=zeros([1,5])
		count_dict[seq][0,1]=float(count)


with open(countfile3,'r') as f:
	for line in f:
		line1=line.split("\t")
		seq=line1[1]
		count=line1[0]
		nreads3=nreads3+float(count)
		seq=seq.strip('\n')
		if not seq in count_dict:
			count_dict[seq]=zeros([1,5])
		count_dict[seq][0,2]=float(count)

with open(countfile4,'r') as f:
	for line in f:
		line1=line.split("\t")
		seq=line1[1]
		count=line1[0]
		nreads4=nreads4+float(count)
		seq=seq.strip('\n')
		if not seq in count_dict:
			count_dict[seq]=zeros([1,5])
		count_dict[seq][0,3]=float(count)

with open(countfile5,'r') as f:
	for line in f:
		line1=line.split("\t")
		seq=line1[1]
		count=line1[0]
		nreads5=nreads5+float(count)
		seq=seq.strip('\n')
		if not seq in count_dict:
			count_dict[seq]=zeros([1,5])
		count_dict[seq][0,4]=float(count)

nreads_array=[nreads,nreads2,nreads3,nreads4,nreads5]

for seq in count_dict:
	if seq in count_dict:
#		prop1=count_dict[seq]/nreads_array
		prop1=count_dict[seq]
		prop=np.average(prop1)
#		print(str(seq)+"\t"+str(prop1)+"\t"+str(prop)+"\t"+str(count_dict[seq])+"\t"+str(nreads_array)  )
		print(str(seq)+"\t"+str(prop))
