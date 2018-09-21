#!/usr/bin/env python

# pw.py - an insecure password locker program

passwords = {'email': 'lkwejfalskjdfoiawe93i2htASDF', 
             'blog': 'lksjadflkwir244t84923823NNNNN',
             'luggage': '12345'}

from sys import argv, exit
from pyperclip import copy, paste

if len(argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    exit()

account = argv[1]

if account in passwords:
    copy(passwords[account])
    print('password for ' + account + 'copied to clipboard')
else:
    print('there is no password for that account')
