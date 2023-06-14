#!/usr/bin/env python3

from optparse import OptionParser
from Bio import SeqIO
import sys

# THIS IS A MASTER PYTHON SCRIPT FOR RUNNING A REFERENCE BASED RNA-SEQ ANALYSIS

# defining the arguments that need to be passed to the scripts
arguments = OptionParser()

arguments.add_option('-i', '--id', dest='id', help='id of sequence to extract')
arguments.add_option('-r', '--range', dest='range', help='range for whhich to extract')
(options, args) = arguments.parse_args()
if options.id is None or options.range is None:
    # if one of the arguments is missing
    print('\n----------> A mandatory option is missing !\n')  # raise an error
    arguments.print_help()  # and provide the help
    exit(-1)  # exit the script
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
start = int(options.range.split('-')[0])
end = int(options.range.split('-')[1])

for read in SeqIO.parse(sys.stdin, 'fasta'):
    if read.id == options.id:
        print('>%s\n%s' % (read.id, str(read.seq)[start:end]))