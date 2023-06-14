#!/usr/bin/env python
from optparse import OptionParser
import sys
import re
# defining the arguments which can be passed to the script
arguments = OptionParser()
arguments.add_option('-r', '--range', dest='range', help='range for which to extract rows')
(options, args) = arguments.parse_args()
if options.range is None:  # if one of the arguments is not provided
        print('\n----------> A mandatory option is missing !\n')   # raise an error

        arguments.print_help()  # and provide the help
        exit(-1)  # exit the script
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

range = options.range.split('-')
range = [int(x) for x in range]
print(range)

for line in sys.stdin:
    if line[0] == '#':
        continue
    else:
        items = line.split()
        #print(items)
        if range[0] <= int(items[3]) and int(items[4]) >= range[1]:
            print('\t'.join(items))