#!/usr/bin/python

import os, sys, re
import pycurl
import cStringIO
import json

class Smushit:
    def __init__(self):
        self.SMUSH_URL = 'http://www.smushit.com/ysmush.it/ws.php?'
        self.fileName = ''
        self.url = ''
        self.compressedUrl = ''
        self.size = None
        self.compressedSize = None
        self.savings = None
        self.id = None
        self.error = None

    def process(self, srcImage, destImage):
        if re.match('https?://', srcImage):
            self.smushURL(srcImage, destImage)
        else:
            self.smushFile(srcImage, destImage)

    def smushURL(self, srcImage, destImage):
        self.url = srcImage
        sf = cStringIO.StringIO()
        pyc = pycurl.Curl()
        pyc.setopt(pycurl.URL, self.SMUSH_URL + 'img=' + srcImage)
        pyc.setopt(pycurl.WRITEFUNCTION, sf.write)
        pyc.setopt(pycurl.CONNECTTIMEOUT, 5)
        pyc.perform()
        pyc.close()
        response = sf.getvalue()
        return self.parseResponse(response, destImage)
    """
    def smushFile(self, arg):
        self.fileName = arg
        pyc = pycurl.Curl()
        pyc.setopt(pycurl.URL, self.SMUSH_URL)
        pyc.setopt(pycurl.RETURNTRANSFER, 1)
        pyc.setopt(pycurl.CONNECTTIMEOUT, 5)
        pyc.setopt(pycurl.POST, True)
        pyc.setopt(pycurl.POSTFIELDS, {'files':arg})
        res = pyc.perform()
        pyc.close()
        return self.parseResponse(res)
    """
    def parseResponse(self, response, destImage):
        if not response:
            self.error = 'No response from Smush.it'
            return False

        response = json.loads(response)
        
        if 'error' in response:
            self.error = response['error']
            return False
        
        self.url = response['src']
        self.size = response['src_size']
        self.compressedUrl = response['dest']
        self.compressedSize = response['dest_size']
        self.savings = response['percent']
        self.id = response['id']
        return self.download(self.compressedUrl, destImage)

    def download(self, url, destImage):
        pyc = pycurl.Curl()
        pyc.setopt(pycurl.URL, url)
        with open(destImage, 'wb') as image:
            pyc.setopt(pycurl.WRITEFUNCTION, image.write)
            pyc.perform()
            pyc.close()
        
if __name__ == '__main__':
    smushit = Smushit()
    try:
        smushit.process(sys.argv[1], sys.argv[2])
    except IndexError:
        print 'Usage: %s <image url or image file path> <target image name>' % sys.argv[0]
        raise SystemExit
