#!/usr/bin/env python3
#This was written for a very specific purpose and works in very particular
#circumstances. See README.md for more info

import os
import shutil
import subprocess
import sys
import time
import urllib.request, urllib.error, urllib.parse, string, itertools, random, csv
import settings, rsstemplate
from subprocess import call

links_folder = os.path.join(settings.blog_folder, 'links')

frag_length = settings.frag_length

html_template = """
        <html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title></title>
    <META HTTP-EQUIV="Refresh" CONTENT="0;URL=%s">
    <meta name="robots" content="noindex"/>
    <link rel="canonical" href="%s"/>
</head>
    <body>

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
"""

# split this so that I don't have to escape all the % above
html_template += """
  ga('create', '%s', 'cloudvent.net');
  ga('send', 'pageview');

</script>

    </body>
</html>
""" % settings.google_analytics_id

try:
    url = sys.argv[1]
    desc = sys.argv[2]
except:
    print("Usage: linkit <URL> <DESC> [<COMMENT>]")
    print(links_folder)
    sys.exit(1)

try:
    comment = sys.argv[3]
except:
    comment = ''

csv_file = open('%s/links.csv' % links_folder)
shorts = dict([(part[0].lower(),part[1]) for part in [line.split(';') for line in csv_file]])
shorts_reversed = dict(list(zip(list(shorts.values()),list(shorts.keys()))))
csv_file.close()


new_frag = False
frag = shorts_reversed.get(url,None)

if not frag:
    new_frag = True
    possible_frags = set(["%s%s" % frag for frag in itertools.permutations(string.ascii_lowercase + string.digits, frag_length)])
    used_frags = set([f for f in os.listdir(links_folder) if '.' not in f] + list(shorts.keys()))
    available_frags = list(possible_frags - used_frags)
    if len(available_frags) < 1:
        print("Time to adjust frag_length to %s" % (frag_length + 1))
    else:
        frag = random.choice(available_frags)
        csv_file = open('%s/links.csv' % links_folder, "a+")
        csv_line = "%s;%s;%s;%s" % (frag, url, desc, comment)
        print(csv_line)
        print(csv_line, file=csv_file)
        csv_file.close()
        os.mkdir("%s/%s" % (links_folder, frag))
        html_file = open("%s/%s/index.html" % (links_folder, frag), "w+")
        print(html_template % (url, url), file=html_file)
        html_file.close()
xml_filename = "%s/%s" % (links_folder, settings.xml_file)
xml_file = open(xml_filename, "w+")
csv_file = open('%s/links.csv' % links_folder)
entries = csv_file.readlines()[-30:]
entries.reverse()
entry_tuples = []
for e in [entry.strip().split(';') for entry in entries]:
    print(e)
    e_code, e_url, e_title, e_desc = e
    if not e_desc:
        e_desc = e_title
    entry_tuples.append((e_title, e_desc, e_code, e_code, e_url))
print(rsstemplate.rsstemplate % "\n".join(
        [rsstemplate.entrytemplate % e for e in entry_tuples]
    ), file=xml_file)
xml_file.close()
print("%s.bsoi.st" % frag)

if new_frag:
    import buildhtml
    buildhtml.build_html()
    os.chdir(settings.blog_folder)
    subprocess.call('git add links'.split())
    subprocess.call(['git', 'commit', '-m', f'Add {frag} short url'])
    subprocess.call('git push'.split())
