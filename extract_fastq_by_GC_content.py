#!/usr/bin/env python3

from optparse import OptionParser
from Bio import SeqIO
from Bio import  SeqUtils

# defining the arguments that need to be passed to the script
arguments = OptionParser()
arguments.add_option('-f', '--file', dest='file', help='input fastq file')
arguments.add_option('-r', '--range', dest='range', help='range of mean GC content for which to extract reads, range is between 0 and 1')
arguments.add_option('-o', '--output', dest='output', help='output name, has to be in fastq format')
(options, args) = arguments.parse_args()
if not options.file or not options.range or not options.output:
    # if one of the arguments is missing
    print('\n----------> A mandatory option is missing !\n')  # raise an error
    arguments.print_help()  # and provide the help
    exit(-1)  # exit the script

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
with open(options.output , 'w') as out_f:
    for read in SeqIO.parse(options.file, 'fastq'):
    #print(read.id, read.seq)
        GC_start = float(options.range.split('-')[0])
        GC_end = float(options.range.split('-')[1])
        #print(GC_start, GC_end)
        GC_proportion = SeqUtils.gc_fraction(str(read.seq), "ignore")
        #print(GC_proportion)
        if GC_start<=GC_proportion<=GC_end:
            SeqIO.write(read, out_f, 'fastq')
