#!/bin/bash
curl --silent -H "If-Modified-Since: `cat mod_date.txt`" http://links.cloudvent.net/config_file.txt >remote_config.txt


if [[ -s remote_config.txt ]] ; then
        diff local_config.txt remote_config.txt |patch local_config.txt
        cp local_config.txt /etc/apache2/sites-available/links.conf
        service apache2 reload
        curl --silent -I http://links.cloudvent.net/config_file.txt |grep Last-Modified |awk '{for (i=2; i<NF; i++) printf $i " "; print $NF}' >mod_date.txt
fi ;

