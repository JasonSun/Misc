#!/usr/bin/python

import sys
import os
import fileinput
import shutil

'''
If only one target header file to be parsed, could use open() instead of fileinput.input().
fileinput.input() could be used to handle many target input files specified in sys.argv[1:]

fileinput.input([files[, inplace[, backup...]]]), set inplace=1 means that standard out will be written into input files
'''
for line in fileinput.input('XLError.h', 1):
	if line.startswith('#define'):
		l = line.split()
		s = l[1] + ' = ' + l[2]
		print s

# shutil module is used to deal with file operations
# shutil.move(src, dest) renames file or directory
shutil.move('XLError.h', 'XLError.py')
