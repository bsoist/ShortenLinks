#!/usr/bin/env python
"""
See README for information on how this is used.
"""
import os

print """Location: http://links.cloudvent.net/%s

""" % os.environ['HTTP_HOST'].split('.')[0]

