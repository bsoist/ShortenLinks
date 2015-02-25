#!/usr/bin/env python
#This was written for a very specific purpose and works in very particular
#circumstances. See README.md for more info
import os, sys, shutil, time
import urllib2, string, itertools, random, csv
import settings, rsstemplate
import folder2s3

links_folder = os.path.join(settings.dropbox_location, "Apps", "Cloud Cannon", settings.cloud_cannon_folder)
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
    print "Usage: linkit <URL> <DESC>";
    print links_folder
    sys.exit(1)

csv_file = open('%s/links.csv' % links_folder)
shorts = dict([(line[0].lower(),line[1]) for line in list(csv.reader(csv_file))])
shorts_reversed = dict(zip(shorts.values(),shorts.keys()))
csv_file.close()

frag = shorts_reversed.get(url,None)

if not frag:
    possible_frags = set(["%s%s" % frag for frag in itertools.permutations(string.lowercase + string.digits, frag_length)])
    used_frags = set([f for f in os.listdir(links_folder) if '.' not in f] + shorts.keys())
    available_frags = list(possible_frags - used_frags)
    if len(available_frags) < 1:
        print "Time to adjust frag_length to %s" % (frag_length + 1)
    else:
        frag = random.choice(available_frags)
        csv_file = open('%s/links.csv' % links_folder, "a+")
        print >>csv_file, "%s,%s,%s" % (frag,url,desc)
        csv_file.close()
        os.mkdir("%s/%s" % (links_folder, frag))
        html_file = open("%s/%s/index.html" % (links_folder, frag), "w+")
        print >>html_file, html_template % (url, url)
        html_file.close()
xml_filename = "%s/%s" % (links_folder, settings.xml_file)
xml_file = open(xml_filename, "w+")
csv_file = open('%s/links.csv' % links_folder)
entries = csv_file.readlines()[-30:]
entries.reverse()
print >>xml_file, rsstemplate.rsstemplate % "\n".join(
        [rsstemplate.entrytemplate % (e[2], e[0], e[0], e[1]) for e in [entry[:-1].split(',') for entry in entries]]
    )
xml_file.close()
print "%s.bsoi.st" % frag

bucket = folder2s3.getBucket("links.bsoi.st","bsoist")
from boto.s3.key import Key
key = Key(bucket)
key.key = "feed.xml"
xml_file = open(xml_filename)
key.set_contents_from_file(xml_file)
key.set_acl("public-read")

