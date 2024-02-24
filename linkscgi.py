#!/usr/bin/env python
#This was written for a very specific purpose and works in very particular
#circumstances. See README.md for more info
import os

print("""Location: http://links.cloudvent.net/%s

""" % os.environ['HTTP_HOST'].split('.')[0])

