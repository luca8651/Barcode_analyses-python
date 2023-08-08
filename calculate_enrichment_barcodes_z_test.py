##!/usr/bin/env python3.5

import os
import re
import sys
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


#script to check for presence and count a set of barcodes in a file
#usage: calculate_enrichment_barcodes_z_test.py  countfile  countfile2


countfile = sys.argv[1]
countfile2 = sys.argv[2]

cont=0

count_dict = dict([])
seq_dict= dict([])

count_dict2 = dict([])
seq_dict2= dict([])

nobs=0

with open(countfile,'r') as f:
	for line in f:
		line1=line.split("\t")
		seq=line1[1]
		count=line1[0]
		nobs=nobs+int(count)
		seq=seq.strip('\n')
		count_dict[seq]=int(count)
nobs2=0
with open(countfile2,'r') as f:
	for line in f:
		line1=line.split("\t")
		seq=line1[1]
		count=line1[0]
		nobs2=nobs2+int(count)
		seq=seq.strip('\n')
		count_dict2[seq]=int(count)


for seq in count_dict2:
	if seq in count_dict:
		prop=count_dict[seq]/nobs
		count=count_dict[seq]
		count2=count_dict2[seq]
		stat, pval = proportions_ztest(count2,nobs2,prop,'larger')
#		pval=str('{0:0.3f}'.format(pval))
		print(str(seq)+"\t"+str(count)+"\t"+str(count2)+"\t"+str(nobs)+"\t"+str(nobs2)+"\t"+str(pval)  )


