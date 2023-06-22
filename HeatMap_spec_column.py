#!/usr/bin/env python3

from optparse import OptionParser
import pandas
import seaborn
import matplotlib.pyplot as plt

# defining the arguments that need to be passed to the script
arguments = OptionParser()
arguments.add_option('-f', '--file', dest='file', help='input csv file')
arguments.add_option('-c', '--columns', dest='columns', help='pattern to look for in columns')
arguments.add_option('-p', '--pdf', dest='pdf', help='pdf output name')

(options, args) = arguments.parse_args()
if not options.columns or not options.pdf or not options.file:
    # if one of the arguments is missing
    print('\n----------> A mandatory option is missing !\n')  # raise an error
    arguments.print_help()  # and provide the help
    exit(-1)  # exit the script

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

file = pandas.read_csv(options.file)
#print(file)

column_names = [col for col in file.columns if options.columns in col]
#print(column_names)
genes = file['gene_ID'].tolist()
#print(genes)
data_subset = file[column_names]
#print(data_subset)
data = []

for ind, row in data_subset.iterrows():
    #print(ind,row)
    data.append(row.tolist())
#print(data)

seaborn.set_context("paper", font_scale=0.3)
sns_plot = seaborn.clustermap(data, xticklabels=column_names, yticklabels=genes)
sns_plot.savefig(options.pdf)

plt.show()

