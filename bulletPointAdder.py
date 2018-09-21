#!/usr/bin/env python

# bulletPointAdder.py = Adds Wikipeida bullet points to the start of each 
#                       line of text on the clipboard

from pyperclip import copy, paste

text = paste()

lines = text.split('\n')

lines[:] = ['* ' + line for line in lines]

text = '\n'.join(lines)

copy(text)