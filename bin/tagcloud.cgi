#!/bin/bash -euxv
source "$(dirname $0)/conf"
exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

tac "$datadir/keyword_list"                                                |
grep -oE ",.+,"                                                            |
cut -d"," -f2-                                                             |
sed -e "s/,$//g" -e "s/,/\n/g"					           |
sort                                                                       |
uniq -c                                                                    |
sort -k1,1 -r                                                              |
awk '{print "<a href=\"/key.cgi?key=" $2 "\">" $2  "(" $1 ")</a><br />" }' |
sed '1iContent-Type: text/html\n\n<h2>Tag Cloud</h2>'
