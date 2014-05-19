#!/usr/bin/python
# python wrapper for Tumblr API

# for POSTFIELDS
import pycurl
from urllib import urlencode

# for postfields and post files
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

from datetime import datetime

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

try:
    import simplejson as json
except ImportError:
    import json

'''
Error Block
'''
# General Error to be inherited
class Error(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return self.err

# RequestError inherite Error
class RequestError(Error):
    pass

# AuthError inherite Error
class AuthError(Error):
    pass

'''
API Class
'''
# class API wraps all methods of Tumblr
class API:
    # tumblr_name is part of url of your tumblr
    # like http://tumblr_name.tumblr.com
    def __init__(self, tumblr_name):
        self.tumblr_name = tumblr_name

    def _auth(self, email, pwd):
        c = pycurl.Curl()
        c.setopt(pycurl.URL, 'http://www.tumblr.com/api/authenticate')
        c.setopt(pycurl.POST, 1)
        # Be careful here, to do POSTFIELDS, you must urlencode the data to be posted.
        c.setopt(pycurl.POSTFIELDS, urlencode({'email': email, 'password': pwd}))
        c.perform()
        response_status_code = c.getinfo(pycurl.RESPONSE_CODE)
        c.close()
        if response_status_code != 200:
            raise AuthError('Auth Error!HTTP status code %d returned.' % response_status_code)
        return True

    '''
        Read Block includes
        ------------------------------------------
        read_by_id()
            Mandatory: id
            optional: None
        read_by_type()
            mandatory: type
            optional: start, num, tagged
        read_by_tags()
            mandatory: tagged
            optional: start, num, type
    '''
    def _read(self, path, query):
        stream = StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, path + query)
        c.setopt(pycurl.WRITEFUNCTION, stream.write)
        c.perform()
        response_status_code = c.getinfo(pycurl.RESPONSE_CODE)
        if response_status_code != 200:
            raise RequestError('Error!Http status code %d returned.' % response_status_code)
        c.close()
        return stream.getvalue()

    def read_by_id(self, **kwargs):
        if 'id' not in kwargs:
            raise RequestError('Post id which is a mandatory param is not supplied.')
        query_str = urlencode(kwargs)
        json_str = self._read(self.tumblr_name + '/api/read/json?debug=1&', query_str)
        json_obj = json.loads(json_str)
        return json_obj

    def read_by_type(self, **kwargs):
        if 'type' not in kwargs:
            raise RequestError('Post type which is a mandatory param is not supplied.')
        kwargs.setdefault('start', 0)
        if kwargs['start'] > 1000:
            raise RequestError("Maximum 'start' param is 1000.")
        kwargs.setdefault('num', 20)
        if kwargs['num'] > 50:
            raise RequestError("Maximum 'num' param is 50.")
        query_str = urlencode(kwargs)
        json_str = self._read(self.tumblr_name + '/api/read/json?debug=1&', query_str)
        json_obj = json.loads(json_str)
        return json_obj

    def read_by_tags(self,**kwargs):
        if 'tagged' not in kwargs:
            raise RequestError('Post tags which must be supplied.')
        kwargs.setdefault('start', 0)
        if kwargs['start'] > 1000:
            raise RequestError("Maximum 'start' param is 1000.")
        kwargs.setdefault('num', 20)
        if kwargs['num'] > 50:
            raise RequestError("Maximum 'num' param is 50.")
        query_str = urlencode(kwargs)
        json_str = self._read(self.tumblr_name + '/api/read/json?debug=1&', query_str)
        json_obj = json.loads(json_str)
        return json_obj

    def read_liked_posts(self, email, pwd, **kwargs):
        kwargs.setdefault('start', 0)
        if kwargs['start'] > 1000:
            raise RequestError("Maximum 'start' param is 1000.")
        kwargs.setdefault('num', 20)
        if kwargs['num'] > 50:
            raise RequestError("Maximum 'num' param is 50.")
        if email == None or pwd == None:
            raise RequestError('Email and Password must be supplied for authenticate.')
        self._auth(email, pwd)
        query_str = urlencode(kwargs)
        json_str = self._read('http://www.tumblr.com/api/likes/json', query_str)
        json_obj = json.loads(json_str)
        return json_obj

    '''
    Read pages return XML format documents
    '''
    def read_pages(self):
        xml_obj = self._read(self.tumblr_name + '/api/pages', '')
        '''
        TODO XML format documents
        '''

    def delete_post(self, email, password, post_id):
        c = pycurl.Curl()
        c.setopt(pycurl.URL, 'http://www.tumblr.com/api/delete')
        c.setopt(pycurl.POST, 1)
        params = {
                'email': email,
                'password': password,
                'post-id': post_id
            }
        c.setopt(pycurl.POSTFIELDS, urlencode(params))
        c.perform()
        c.close()

    '''
    Write Block includes
    ------------------------------
    write_regular()
    write_quote()
    write_link()
    write_conversation()
    write_photo()
    write_video()
    write_audio()
    '''
    def _write(self, params):
        if 'email' not in params or 'password' not in params:
            raise AuthError('Must supply your email and password for Authentication.')
        params.setdefault('date', datetime.now())
        params.setdefault('private', 0)
        params.setdefault('tags', None) # comma-separated list
        if params['tags'] != None and (isinstance(params['tags'], list) != True):
            raise RequestError('param tags must be a list object')
        params.setdefault('slug', None)
        params.setdefault('state', 'published')
        if 'data' not in params:
            c = pycurl.Curl()
            c.setopt(pycurl.POST, 1)
            c.setopt(pycurl.URL, 'http://www.tumblr.com/api/write')
            c.setopt(pycurl.POSTFIELDS, urlencode(params))
            c.perform()
            response_status_code = c.getinfo(pycurl.RESPONSE_CODE)
            if response_status_code != 201:
                raise RequestError('Error!Http status code %d returned.' % response_status_code)
            c.close()
        else:
            # code of this line is used to reconstruct params removing items whose value is None
            # poster.encode.multipart_encode() accept dict with no None value items
            params = dict((k, v) for k, v in params.iteritems() if v)
            register_openers()
            datagen, headers = multipart_encode(params)
            request = urllib2.Request('http://www.tumblr.com/api/write', datagen, headers)
            try:
                urllib2.urlopen(request)
            except urllib2.HTTPError, e:
                raise RequestError('Error!Http status code %d returned.' % e.code)

    '''
    require at least one: title, body
    '''
    def write_regular(self, title = None, body = None, **kwargs):
        kwargs['type'] = 'regular'
        if title == None and body == None:
            raise RequestError('Write regular post needs one of title and body params.')
        if title:
            kwargs['title'] = title
        if body:
            kwargs['body'] = body
        return self._write(kwargs) # return post id if successfully write

    '''
    mandatory: quote
    optional: source
    '''
    def write_quote(self, quote, source = None, **kwargs):
        kwargs['type'] = 'quote'
        if not quote:
            raise RequestError('Writing quote post, you must supply quote param.')
        kwargs['quote'] = quote
        if source:
            kwargs['source'] = source
        return self._write(kwargs)

    '''
    mandatory: url
    optional: name, description
    '''
    def write_link(self, url, name = None, description = None, **kwargs):
        kwargs['type'] = 'link'
        if not url:
            raise RequestError('Writing link post, you must supply url param.')
        kwargs['url'] = url
        if name:
            kwargs['name'] = name
        if description:
            kwargs['description'] = description
        return self._write(kwargs)

    '''
    mandatory: conversation
    optional: title
    '''
    def write_conversation(self, conversation, title = None, **kwargs):
        kwargs['type'] = 'conversation'
        if not conversation:
            raise RequestError('Writing conversation post, you must supply conversation param.')
        kwargs['conversation'] = conversation
        if title:
            kwargs['title'] = title
        return self._write(kwargs)

    '''
    mandatory: source or data (if both, source will be used)
    optional: caption, click-through-url
    '''
    def write_photo(self, source = None, data = None, caption = None, click_through_url = None, **kwargs):
        kwargs['type'] = 'photo'
        if not source and not data:
            raise RequestError('Writing photo, you must supply one of source and data. If both, source preferred.')
        if source:
            kwargs['source'] = source
        else:
            kwargs['data'] = open(data, 'rb')
        if caption:
            kwargs['caption'] = caption
        if click_through_url:
            kwargs['click-through-url'] = click_through_url
        return self._write(kwargs)

    '''
    mandatory: embed or data, but not both
    optional: title, caption
    '''
    def write_video(self, embed = None, data = None, title = None, caption = None, **kwargs):
        kwargs['type'] = 'video'
        if (not embed and not data) or (embed and data):
            raise RequestError('Writing video, you must specify one of embed and data, not both.')
        if embed:
            kwargs['embed'] = embed
        else:
            kwargs['data'] = open(data, 'rb')
        if title:
            kwargs['title'] = title
        if caption:
            kwargs['caption'] = caption
        return self._write(kwargs)

    '''
    mandatory: data or externally-hosted-url, but not both
    optional: caption
    '''
    def write_audio(self, data = None, externally_hosted_url = None, caption = None, **kwargs):
        kwargs['type'] = 'audio'
        if (not data and not externally_hosted_url) or (data and externally_hosted_url):
            raise RequestError('Writing audio, you must specify one of data and external, not both')
        if data:
            kwargs['data'] = open(data, 'rb')
        else:
            kwargs['externally-hosted-url'] = externally_hosted_url
        if caption:
            kwargs['caption'] = caption
        return self._write(kwargs)
