#!/bin/bash -euxv
source "$(dirname $0)/conf"
exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

word=$(nkf --url-input <<< ${QUERY_STRING} | sed 's/^key=//')

tac "$datadir/keyword_list"     |
grep -F ",$word,"               |
awk '{print $1}'                |
xargs -I@ cat "$datadir/@/link" |
sed 's/^/* /'                   |
sed "1i# Keyword: $word"        |
pandoc --template="$viewdir/template.html" 
