#!/usr/bin/env python
import os
import settings
from boto.s3.key import Key
import folder2s3

html_template = """<ul id="linkblog">\n%s\n</ul>"""
link_template = '<li><a href="http://%s.bsoi.st" target="_blank">%s</a>%s</li>'

links_folder = os.path.join(
    settings.dropbox_location,
    "Apps",
    "Cloud Cannon",
    settings.cloud_cannon_folder)

def build_html():
    global DEBUG
    csv_file = open("%s/links.csv" % links_folder)
    html_file = open("links.html", "w+")
    data = csv_file.read()
    lines = data.split("\n")
    link_tuples = []
    for line in reversed(lines[12:-1]):
        link_code, link_url, link_title, link_comment = line.split(';')
        if link_comment == link_title:
            link_comment = ''
        if link_comment: # if it's not empty
            link_comment = '<br/><blockquote>%s</blockquote>' % link_comment
        link_tuples.append((link_code, link_title, link_comment))
    html_file.write(
            html_template % "\n".join(
                [link_template % link_tuple for link_tuple in link_tuples]
            )
        )

def save_html():
    bucket = folder2s3.getBucket("links.bsoi.st","bsoist")
    key = Key(bucket)
    key.key = "links.html"
    key.set_contents_from_filename("links.html")
    key.set_acl("public-read")
    key.copy(bucket,key.key, preserve_acl=True, metadata={'Content-type': 'text/html'})

build_html()
save_html()

