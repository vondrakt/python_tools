#!/usr/bin/env python

from optparse import OptionParser
from Bio import SeqIO
# defining the arguments which can be passed to the script
arguments = OptionParser()
arguments.add_option('-f', '--fasta', dest='fasta', help='fasta file to split')
arguments.add_option('-r', '--range', dest='range', help='range of the sequences, format x-y starting from 0')
(options, args) = arguments.parse_args()
if options.fasta is None or options.range is None:  # if one of the arguments is not provided
        print('\n----------> A mandatory option is missing !\n')   # raise an error

        arguments.print_help()  # and provide the help
        exit(-1)  # exit the script
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start = int(options.range.split('-')[0])
end = int(options.range.split('-')[1])

out = open('%s__%s-%s'% (options.fasta,str(start),str(end)), 'w')

with open(options.fasta) as f:
        i = 0
        for sequence in SeqIO.parse(f, 'fasta'):
           if start <= i <= end:
                out.write('>%s\n%s\n'%(sequence.id, str(sequence.seq)))

           i += 1

out.close()