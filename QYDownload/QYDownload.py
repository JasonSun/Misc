#!/usr/bin/python

import sys
from ctypes import * # Calling export functions in DLL needs ctypes module

from XLError import * # XLError.py is generated from 'python HParser.py XLError.h'

def QYDownload(dllObject):
	if dllObject.XLInitDownloadEngine() == False:
		print 'Initialize download engine failed.\n'
		return XL_ERROR_FAIL
	else:
		'''
		All stuff defined here
		'''
		pass

if __name__ == '__main__':
	'''
	use DLL in python
	Be sure zlib1.dll must be loaded before XLDownload.dll
	'''
	cdll.LoadLibrary('E:\Download\Engine\zlib1.dll')
	XLDll = cdll.LoadLibrary('E:\Download\Engine\XLDownload.dll')
	QYDownload(XLDll)
