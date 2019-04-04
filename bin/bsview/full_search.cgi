#!/bin/bash -xv
source "$(dirname $0)/../conf"
exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

word=$(nkf --url-input <<< ${QUERY_STRING} | sed 's/^word=//' )
numchar=$(nkf -w16B0 <<< "$word" | xxd -plain | tr -d '\n' | sed 's/..../\&#x&;/g')

cat << FIN
Content-Type: text/html

<h1>検索結果</h1>
FIN

[ -n "$word" ] &&
tac "$datadir/all_markdown"             |
grep " .*$word"                         |
awk '{print $1}'                        |
uniq                                    |
head -n 100                             |
xargs -I@ cat "$datadir/@/link_date"    |
sed 's;$;<br/>;'
