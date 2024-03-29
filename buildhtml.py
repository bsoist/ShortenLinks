#!/usr/bin/env python
import os
import settings
from boto.s3.key import Key

html_template = """<ul id="linkblog">\n%s\n</ul>"""
link_template = '<li><a href="http://%s.bsoi.st" target="_blank">%s</a>%s</li>'

links_folder = os.path.join(settings.blog_folder, 'links')

def build_html():
    global DEBUG
    csv_file = open(f"{links_folder}/links.csv")
    html_file = open(f"{links_folder}/links.html", "w+")
    data = csv_file.read()
    lines = data.split("\n")
    link_tuples = []
    for line in reversed(lines[12:-1]):
        print(line)
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


