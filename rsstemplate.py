import datetime, settings

details = {
    'author': settings.author,
    'nickname': settings.nickname,
    'email': settings.email,
    'facebook': settings.facebook,
    'twitter': settings.twitter,
    'pic': "http://%s/%s" % (settings.cloud_cannon_url, settings.image),
    'archive': "http://%s/" % settings.cloud_cannon_url,
    'xml_file': settings.xml_file,
    'html_link': "http://%s/%s" % (settings.cloud_cannon_url, settings.html_file),
    'startDate': settings.start_date,
    'pubDate': datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT"),
    'endDate': datetime.datetime.utcnow().strftime("%Y-%m-%d"),
    'localTime': datetime.datetime.utcnow().strftime("%m/%d/%Y; %I:%M:%S %p"),
    'holder':'%s',
}

rsstemplate = '''
<?xml version="1.0"?>
<rss version="2.0" xmlns:source="http://source.smallpict.com/2014/07/12/theSourceNamespace.html">
	<channel>
		<title>%(nickname)s&apos;s linkblog feed</title>
        <link>%(html_link)s</link>
		<description>%(nickname)s&apos;s linkblog.</description>
		<language>en-us</language>
		<pubDate>%(pubDate)s</pubDate>
		<lastBuildDate>%(pubDate)s</lastBuildDate>
                <generator>https://github.com/bsoist/ShortenLinks</generator>
		<docs>http://cyber.law.harvard.edu/rss/rss.html</docs>
		<webMaster>%(email)s (%(author)s)</webMaster>
		<source:account service="facebook">%(facebook)s</source:account>
		<source:account service="twitter">%(twitter)s</source:account>
        <source:avatar>%(pic)s</source:avatar>
		<cloud domain="rpc.rsscloud.org" port="5337" path="/rsscloud/pleaseNotify" registerProcedure="" protocol="http-post" />
		<source:archive>
			<source:url>%(archive)s</source:url>
			<source:filename>%(xml_file)s</source:filename>
			<source:startDay>%(startDate)s</source:startDay>
			<source:endDay>%(endDate)s</source:endDay>
		</source:archive>
		<source:localTime>%(localTime)s</source:localTime>
                %(holder)s
	</channel>
</rss>
''' % details


entrytemplate = '''
		<item>
			<description>%(holder)s</description>
			<link>%(holder)s</link>
			<pubDate>%(pubDate)s</pubDate>
			<guid>%(holder)s</guid>
			<source:linkFull>%(holder)s</source:linkFull>
		</item>
''' % details