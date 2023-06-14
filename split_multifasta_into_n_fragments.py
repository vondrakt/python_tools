#!/usr/bin/env python

from optparse import OptionParser
from Bio import SeqIO
# defining the arguments which can be passed to the script
arguments = OptionParser()
arguments.add_option('-f', '--fasta', dest='fasta', help='fasta file to split')
arguments.add_option('-n', '--number', dest='number', help='number of fragments into which the multifasta will be split')
(options, args) = arguments.parse_args()
if options.fasta is None or options.number is None:  # if one of the arguments is not provided
        print('\n----------> A mandatory option is missing !\n')   # raise an error

        arguments.print_help()  # and provide the help
        exit(-1)  # exit the script
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

with open(options.fasta) as f:
        count = 0
        for sequence in SeqIO.parse(f, 'fasta'):
           count += 1

#print(count)
step = round(count/int(options.number))
#print(step)

ranges = range(0,count+step,step)
i = 0
while i < len(ranges)-1:
        #print(ranges[i], ranges[i+1])
        out = open('./%s__%s-%s' % (options.fasta, str(ranges[i]), str(ranges[i+1])), 'w')
        with open(options.fasta) as f:
                count = 0
                for sequence in SeqIO.parse(f, 'fasta'):
                        if ranges[i] <= count < ranges[i+1]:
                                out.write('>%s\n%s\n' % (sequence.id, str(sequence.seq)))
                        count += 1
        out.close()
        i += 1

