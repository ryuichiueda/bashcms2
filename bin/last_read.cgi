#!/bin/bash
source "$(dirname $0)/conf"
#exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

num=$(tr -dc '0-9' <<< ${QUERY_STRING})
[ -z "$num" ] && num=10

echo "Content-Type: text/html"
echo 
echo "<h1>現在読まれている記事</h1>"

awk '{print $1,$2,$3,$4}' $datadir/journals/journal_$(date "+%Y%m%d") |
sort -k4,4                                             |
tac                                                    |
uniq -f 3                                              |
sort -k1,2                                             |
tail -n "$num"                                         |
tac                                                   |
awk '{print $3,$4}'                                   |
while read s dir ; do
	date "+%H:%M:%S" -d "@$s"
	sed "s;</a>;&<br />;" "$datadir/$dir/link"
done


