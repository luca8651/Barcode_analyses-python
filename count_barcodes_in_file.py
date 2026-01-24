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

cont=0

count_dict = dict([])
seq_dict= dict([])

with open(countfile,'r') as f:
	for line in f:
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
		if seq in count_dict:
			print(count_dict[seq]+"\t"+seq)
		else:
			print("0\t"+seq)
