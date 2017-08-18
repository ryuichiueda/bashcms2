#!/bin/bash -xv
exec 2> /tmp/log
source /var/www/bashcms2/conf

while read url ; do
	page=$(tr -dc 'a-zA-Z0-9_?=/' <<< "$url" | sed 's/.*?//' | sed 's;=;s/;' )
	ls -l "$datadir/counters/$(tr '/' '_' <<<$page)" | cut -d' ' -f 5
done
