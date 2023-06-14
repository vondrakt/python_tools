#!/usr/bin/env python

import sys
from Bio import SeqIO

sum = 0 
for sequence in SeqIO.parse(sys.stdin, 'fasta'):
	sum = sum + len(str(sequence.seq))

print(sum)
