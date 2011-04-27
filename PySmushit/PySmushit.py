#!/usr/bin/python

import os, sys, re
import pycurl
try:
    import cStringIO
except ImportError:
    import StringIO as cStringIO

try:
    import json
except ImportError:
    import simplejson as json

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

    # Dispatch function
    def process(self, srcImage, destImage):
        if re.match('https?://', srcImage):
            self.smushURL(srcImage, destImage)
        else:
            self.smushFile(srcImage, destImage)

    def smushURL(self, srcImage, destImage):
        sf = cStringIO.StringIO()
        pyc = pycurl.Curl()
        pyc.setopt(pycurl.URL, self.SMUSH_URL + 'img=' + srcImage)
        pyc.setopt(pycurl.WRITEFUNCTION, sf.write) # write server response into sf file-like object buffer
        pyc.setopt(pycurl.CONNECTTIMEOUT, 5)
        pyc.perform()
        pyc.close()
        response = sf.getvalue() # get server response, read from sf buffer
        return self.parseResponse(response, destImage)

    def smushFile(self, srcImage, destImage):
        '''
            code snippet explains how to upload image using HTTP POST
            http://code.activestate.com/recipes/576422/
        '''
        sf = cStringIO.StringIO()
        pyc = pycurl.Curl()
        pyc.setopt(pycurl.POST, 1)
        pyc.setopt(pycurl.URL, self.SMUSH_URL)
        pyc.setopt(pycurl.CONNECTTIMEOUT, 5)
        pyc.setopt(pycurl.HTTPPOST, [('files', (pyc.FORM_FILE, srcImage))])
        pyc.setopt(pycurl.WRITEFUNCTION, sf.write)
        pyc.perform()
        pyc.close()
        response = sf.getvalue()
        return self.parseResponse(response, destImage)

    def parseResponse(self, response, destImage):
        if not response:
            self.error = 'No response from Smush.it'
            return False
        '''
            response looks like this:
            '{"src":"...", "src_size":..., "dest":"..."}'

            As we see above, dict object is wrapped into str object.
            We should escape dict from str, How to do? Two solutions below:
            1. use json module, json.loads(str) decodes str
            2. use eval(str), but eval() function is claimed as a security problem
               try use import ast ast.literal_eval() function.
        '''
        response = json.loads(response)
        '''
        import ast
        response = ast.literal_eval(response)
        '''
        
        if 'error' in response: # key in dict
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
        print 'python PySmushit.py www.example.com/image.jpg fromUrl.jpg'
        print 'python PySmushit.py /path/to/image.jpg fromFile.jpg'
        raise SystemExit
