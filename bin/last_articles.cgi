#!/bin/bash
source "$(dirname $0)/conf"
exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

num=$(tr -dc '0-9' <<< ${QUERY_STRING})
[ -z "$num" ] && num=10

tac "$datadir/post_list"		|
head -n "$num"				|
awk '{print $3}'                        |
xargs -I@ cat "$datadir/@/link_date"    |
sed 's;$;<br />;'			|
sed '1iContent-Type: text/html\n\n<h1>Recent posts</h1>'
