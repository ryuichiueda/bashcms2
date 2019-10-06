#!/bin/bash -xv
source "$(dirname $0)/conf"
exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

echo -e 'Content-Type: text/html\n'
sed 's/%2C/\n/g' <<< ${QUERY_STRING}                       |
nkf --url-input                                            |
sed -e '1s/keywords=//' -e 's/^[ 　]*//' -e 's/[ 　]*$//'  |
nkf -w16B0                                                 |
xxd -plain                                                 |
tr -d '\n'                                                 |
sed 's/..../\&#x&;/g'                                      |
sed 's/\&#x000a;/\n/g'                                     |
awk '{print "<a href=\"/key.cgi?key="$1 "\">" $1 "</a>" }' 
