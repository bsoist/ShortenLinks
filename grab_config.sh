#!/bin/bash

#This was written for a very specific purpose and works in very particular 
#circumstances. See README.md for more info

CLOUD_CANNON_URL=http://links.cloudvent.net

curl --silent -H "If-Modified-Since: `cat mod_date.txt`" $CLOUD_CANNON_URL/config_file.txt >remote_config.txt


if [[ -s remote_config.txt ]] ; then
        diff local_config.txt remote_config.txt |patch local_config.txt
        cp local_config.txt /etc/apache2/sites-available/links.conf
        service apache2 reload
        curl --silent -I $CLOUD_CANNON_URL/config_file.txt |grep Last-Modified |awk '{for (i=2; i<NF; i++) printf $i " "; print $NF}' >mod_date.txt
fi ;

