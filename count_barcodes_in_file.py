##!/usr/bin/env python3.5
import csv
import os
import re
import sys
from difflib import ndiff
from difflib import SequenceMatcher

#script to check for presence and count a set of barcodes in a file
#
#usage: count_barcodes_in_file.py barcode_seqq  countfile

#outdir = sys.argv[1]

filename = sys.argv[1]
countfile = sys.argv[2]
#average = int(sys.argv[2])
#min_qual = int(sys.argv[3])
#size = sys.argv[2]
#normal=list([''])
#tumor=list([''])

cont=0
#cont2=0

count_dict = dict([])
seq_dict= dict([])

with open(countfile,'r') as f:
	for line in f:
		#reader=csv.reader(line,delimiter='\t')
		line1=line.split("\t")
		seq=line1[1]
		count=line1[0]
		seq=seq.strip('\n')
		count_dict[seq]=count

with open(filename,'r') as f:
	for line in f:
		seq=line
		seq=seq.strip('\n')
		seq_dict[seq]=seq
#		print("count for seq "+ seq + " is "+count_dict[seq])
		if seq in count_dict:
			print(count_dict[seq]+"\t"+seq)
		else:
			print("0\t"+seq)


		
