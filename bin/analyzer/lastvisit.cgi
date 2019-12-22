#!/bin/bash
source "$(dirname $0)/../conf"
#exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

num=$(tr -dc '0-9' <<< ${QUERY_STRING})
[ -z "$num" ] && num=10

echo "Content-Type: text/html"
echo 

tail -n "$num" $datadir/journals/journal_$(date "+%Y%m%d") |
tac                                                        |
awk '{print $2,$4}'                                        |
while read s dir ; do
	date "+%H:%M:%S" -d "@$s"
	sed "s;</a>;&<br />;" "$datadir/$dir/link"
done


