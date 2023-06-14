#!/usr/bin/env python

import sys
from Bio import SeqIO

for sequence in SeqIO.parse(sys.stdin, 'fasta'):
    print('>%s' % sequence.id)
    print(len(str(sequence.seq)))