
"""
Usage:
    see mongoexport_docsize_analyze.sh in this directory
"""

__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com"
__license__ = "MIT"
__version__ = "November 2021"

import os
import sys
import time
import traceback

import numpy as np
import pandas as pd

from docopt import docopt

csv_file = 'tmp/docsize_extract.csv'

def docsize_extract(infile):
    # read infile line-by-line
    # create a corresponding csv outfile with three fields; row_index, doc_size, large_ind
    # then, docsize_analysis() will read the csv file and process it with pandas
    print('docsize_extract: {}'.format(infile), file=sys.stderr)
    max_doc_size = megabyte() * 2
    print('max_doc_size: {}'.format(max_doc_size), file=sys.stderr)

    print('row_index,doc_size,large_ind')  # redirected csv header row

    it = text_file_iterator(infile)
    for i, line in enumerate(it):
        size = len(line)
        large_ind = 0
        if size > max_doc_size:
            large_ind = 1
        print('{},{},{}'.format(i, size, large_ind))  # redirected csv detail row

def docsize_analysis():
    print('docsize_analysis: {}'.format(csv_file), file=sys.stderr)

    df = pd.read_csv(csv_file, sep=',', header=0)

    large_df = df[df['large_ind'] > 0] 
    large_doc_count = large_df.shape[0]

    print('row/doc count:   {}'.format(df.shape[0]), file=sys.stderr)
    print('large doc count: {}'.format(large_doc_count), file=sys.stderr)
    print('max doc size:    {}'.format(df['doc_size'].max()), file=sys.stderr)
    print('avg doc size:    {}'.format(df['doc_size'].mean()), file=sys.stderr)
    print('min doc size:    {}'.format(df['doc_size'].min()), file=sys.stderr)

def text_file_iterator(infile):
    # return a line generator that can be iterated with iterate()
    with open(infile, 'rt') as f:
        for line in f:
            yield line.strip()

def describe_df(df, msg):
    print('=== describe df: {}'.format(msg), file=sys.stderr)
    print(str(type(df)))  # <class 'pandas.core.frame.DataFrame'>
    print('--- df.dtypes', file=sys.stderr)
    print(df.dtypes)
    print('--- df.shape', file=sys.stderr)
    print(df.shape)

def megabyte():
    return pow(1024, 2)

def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version=__version__)
    print(arguments)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        func = sys.argv[1].lower()

        if func == 'docsize_extract':
            infile = sys.argv[2]
            docsize_extract(infile)
        elif func == 'docsize_analysis':
            docsize_analysis()
        else:
            print_options('Error: invalid command-line function: {}'.format(func))
    else:
        print_options('Error: no command-line function given')
