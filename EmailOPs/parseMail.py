#!/usr/bin/python

import email

# instantiate an email message object via 'email.message_from_file()'
# open with r mode before using it
with open('email', 'r') as fp:
    msg = email.message_from_file(fp)

# email message object consists of headers and payloads
# in payloads, there might be one or more message objects recursively
# so we will check message object whether multiparts exist
if msg.is_multipart():
    
    # get_payload() returns one string if only one part exists
    # else return a list of message objects in payload
    print 'This email message contains %d parts(Message Objects).' % len(msg.get_payload())
    print 'From: ' + msg['from']
    print 'To: ' + msg['to']
    print 'Subject: ' + msg['subject']

    # iterate the multiparts in payloads
    # part is also Message object
    for part in msg.get_payload():
        if part.get_content_type() == 'text/plain':
            processText(part.get_payload())
        if part.get_content_tyep == 'text/html':
            processHtml(part.get_payload())

# only one part in payload, get_payload() returns string
else:
    print msg.get_payload().strip()
