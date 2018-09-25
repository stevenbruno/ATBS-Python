#!/usr/bin/env python

# this script removes the quiz and answer files 
# generated in randomQuizGenerator.py

import os

for file in os.listdir():
    if file.startswith('capitals'):
        os.remove(file)

print('files removed')