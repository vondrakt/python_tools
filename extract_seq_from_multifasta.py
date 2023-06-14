#!/usr/bin/env python3

from optparse import OptionParser
from Bio import SeqIO
import sys

# THIS IS A MASTER PYTHON SCRIPT FOR RUNNING A REFERENCE BASED RNA-SEQ ANALYSIS

# defining the arguments that need to be passed to the scripts
arguments = OptionParser()

arguments.add_option('-i', '--id', dest='id', help='id of sequence to extract')
(options, args) = arguments.parse_args()
if options.id is None:
    # if one of the arguments is missing
    print('\n----------> A mandatory option is missing !\n')  # raise an error
    arguments.print_help()  # and provide the help
    exit(-1)  # exit the script
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for read in SeqIO.parse(sys.stdin, 'fasta'):
    if read.id == options.id:
        print('>%s\n%s' % (read.id, str(read.seq)))