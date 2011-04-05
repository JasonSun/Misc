#!/usr/bin/python

import sys
import smtplib
from getpass import getpass
import email

fromAddr = raw_input()
toAddrs = raw_input().split()
pwd = getpass()

try:
    sendServer = smtplib.SMTP_SSL('smtp.gmail.com', 465)
except SMTPException:
    exit(1)

sendServer.set_debuglevel(1)

try:
    sendServer.login(fromAddr, pwd)
except SMTPAuthenticationError, SMTPHeloError:
    exit(1)

# Use EMAIL module to generate msg
msg = '...'
    
sendServer.sendmail(fromAddr, toAddrs, msg)
sendServer.quit()
