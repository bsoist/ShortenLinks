#This was written for a very specific purpose and works in very particular
#circumstances. See README.md for more info
import os

home_folder = os.environ.get("HOME") or os.environ.get("HOMEPATH")
blog_folder = os.path.join(home_folder, 'code', 'bsoist.github.io')

short_url = "bsoi.st"
google_analytics_id = "UA-7456633-8"
author = "Bill Soistmann"
nickname = "bsoist"
email = "bsoist@whsjr.soistmann.com"
facebook = "bsoist"
twitter = "bsoist"
start_date = "2014-01-01"
html_url = "http://www.bsoi.st/links/"
archive_url = html_url
image_url = "http://www.bsoi.st/images/me.jpg"
xml_file = "rss.xml"
frag_length = 2
