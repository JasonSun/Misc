#!/usr/bin/python

import sys # Could also pass gmail address and password via sys.argv[]
from getpass import getpass # Getpass.getpass() function is used for entering password invisibly
import poplib # POP protocol client
import email
import email.generator

# Input gmail address like 'username@gmail.com'
gmailAddr = raw_input('Gmail Address:')

# Input invisible gmail password in console via getpass() function
gmailPwd = getpass()

# Instantiate an POP3 instance using SSL
recvServer = poplib.POP3_SSL('pop.gmail.com', 995) # Gmail POP3 server SSL port #995

# Set debug level, 0: default, 1: output moderate debug infos, just 1 line
recvServer.set_debuglevel(1)

# Connect POP server using customer's personal gmail address and password
recvServer.user(gmailAddr)
recvServer.pass_(gmailPwd)

 # Return greeting string sent by POP3 server
greeting = recvServer.getwelcome()
print greeting

 # Return (response, [mailNum: octet, ...], octets), octet is the size of a mail
print recvServer.list()

 # Return a tuple (mail counts, size of your mailbox)
mailboxStatus = recvServer.stat()
print mailboxStatus

# Retrieve the ith mail details using retr() function and the first mail returned in this example
# Details need to be parsed using EMAIL module
details = recvServer.retr(mailboxStatus[0])[1] # Return (response, [line, ...], octets)

# Be sure to join line list with newline'\r\n' symbol
# After completely join action, email message string is gained.
s = '\r\n'.join(details)

'''
# write email message string into email message file so-called
with open('email_latest', 'w') as fp: # when use 'with...as' statement, user avoid calling fp.close() explicitly
    fp.write(s)
'''

# generate flat text of email message represented by email message object structure
# use email.generator.Generator(outfp).flatten(msg)
msg = email.message_from_string(s)
with open('email_latest', 'w') as outfp:
    gen = email.generator.Generator(outfp)
    gen.flatten(msg)
