##!/usr/bin/env python3.5
import csv
import os
import re
import sys
from difflib import ndiff
from difflib import SequenceMatcher

#script to identify and separate sequences which have a hamming distance (from the cluster consensus seq) 
#higher than 2, and/or seem to differ by some indel operations.

if len(sys.argv)<2:
	print("usage: filter_starcount_cluster_counts_input_distance.py starcount_cluster  countfile distance freq")
	print("\tstarcount_cluster: tab delimited output of starcount clustering algorithm")
	print("\tcountfile: tab delimited file with counts stored in column 1 and ids stored in column 2")
	print("\tdistance: max hamming distance allowed between a secondary sequence and the cluster reference")
	print("\tfreq: minimum count for a sequence to be removed from its cluster")
	sys.exit(1)

#outdir = sys.argv[1]

filename = sys.argv[1]
countfile = sys.argv[2]

distance=1
if len(sys.argv)>3:
	distance=sys.argv[3]

freq=8

if len(sys.argv)>4:
	freq=sys.argv[4]

distance=int(distance)
freq=int(freq)

#print("hhheeey "+str(distance)+" "+str(freq))

cont=0
#cont2=0

count_dict = dict([])


with open(countfile,'r') as f:
	for line in f:
		line1=line.split("\t")
		seq=line1[1]
		seq=seq.strip('\n')
		count=line1[0]
		count_dict[seq]=count
#		print("count for seq "+ seq + " is "+count_dict[seq])



with open(filename,'r') as f:
	for line in f:
		#reader=csv.reader(line,delimiter='\t')
		line1=line.split("\t")
		consensus=line1[0]
		count=count_dict[consensus]
		seqq=line1[2]
		seqq=seqq.split(",")
		counts=line1[3]
		counts=counts.split(",")
		newseqq=""
		newcounts=""
		newseqq2=""
		newcounts2=""
		for i in range(1,len(seqq)):         #skip position 0, where the consensus sequence is printed again
#			print(consensus+" "+seqq[i]+" "+str(SequenceMatcher(None,consensus, seqq[i]).ratio() )  )
			diff=ndiff(consensus, seqq[i])
#			print ''.join(diff)
			s = SequenceMatcher(None,consensus, seqq[i])
#			print(s.get_matching_blocks())
#			print(s.get_opcodes())
			op=s.get_opcodes()           #returns list of vectors of length 5, describing the conversion operations
			cont=0
			indel=0
			test=int(count_dict[consensus])/int(count_dict[seqq[i]])
#			print( count_dict[consensus]+ " "+count_dict[seqq[i]]+" "+ str(test) +str(op))
			for k in range(0,len(op)):
#				print(op[k][0])
				if op[k][0]=="replace":
					cont=cont+op[k][2]-op[k][1]    # ["replace",ind11,ind12,ind21,ind22]
				if op[k][0]=="insert":
					indel=indel+op[k][4]-op[k][3]
				if op[k][0]=="delete":
					indel=indel+1+op[k][2]-op[k][1]
#			print("heey "+str(indel)+" "+str(cont))
			if  cont<=distance and indel==0 and test>=freq:
				if len(newseqq)==0:
					newseqq=seqq[i]
					newcounts=count_dict[seqq[i]]
				else:
					newseqq=newseqq+","+seqq[i]
					newcounts=newcounts+","+count_dict[seqq[i]]
			else:
				if len(newseqq2)==0:
					newseqq2=seqq[i]
					newcounts2=count_dict[seqq[i]]
					
				else:
					newseqq2=newseqq2+","+seqq[i]
					newcounts2=newcounts2+","+count_dict[seqq[i]]
		newcounts=newcounts.strip('\n')
		newcounts2=newcounts2.strip('\n')
		print( consensus+"_cons"+"\t"+count+"\t"+newseqq+"\t"+newcounts)
		newseqq2=newseqq2.split(",")
		newcounts2=newcounts2.split(",")
#		print(newseqq2)
		if len(newseqq2[0])>0:
			for k in range(0,len(newseqq2)):
				print(newseqq2[k]+"\t"+newcounts2[k])

	


