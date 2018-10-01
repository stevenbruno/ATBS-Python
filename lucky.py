#!/usr/bin/env python

# lucky.py - opens several google search results.

import requests
import sys
import webbrowser
import bs4

print('Googling...')
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
