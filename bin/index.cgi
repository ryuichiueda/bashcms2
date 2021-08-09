#!/bin/bash -euxv
source "$(dirname $0)/conf"
exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"
set -o pipefail

trap 'rm -f $tmp-*' EXIT

### VARIABLES ###
tmp=/tmp/$$
dir="$(tr -dc 'a-zA-Z0-9_=' <<< ${QUERY_STRING} | sed 's/fbclid=.*//' | sed 's;=;s/;')"
[ -z "$dir" ] && dir="pages/top"
md="$contentsdir/$dir/main.md"
[ -f "$md" ]


### MAKE MATADATA ###
counter="$datadir/counters/$(tr '/' '_' <<< $dir)"
echo -n 1 >> "$counter" # increment the counter

cat << FIN | tee /tmp/hogehoge > $tmp-meta.yaml
---
created_time: '$(LANG=C date -f - < "$datadir/$dir/created_time")'
modified_time: '$(LANG=C date -f - < "$datadir/$dir/modified_time")'
title: '$(cat "$datadir/$dir/title")'
nav: '$(cat "$datadir/$dir/nav")'
views: '$(ls -l "$counter" | cut -d' ' -f 5)'
$(cat $contentsdir/config.yaml )
page: '$(sed 's;s/;=;' <<< $dir)'
---
FIN

REF=$(tr '\n' ' ' <<< ${HTTP_REFERER:=_} | sed 's/  */ /g')
date "+%Y%m%d %H%M%S %s.%N $dir $REF" >> $datadir/journals/journal_$(date "+%Y%m%d")

### OUTPUT ###
pandoc --toc --toc-depth=2 --template="$viewdir/template.html"	\
    -f markdown_github+yaml_metadata_block "$md" "$tmp-meta.yaml"   |
sed -r "/:\/\/|=\"\//!s;<(img src|a href)=\";&/$dir/;g"             |
sed "s;/$dir/#;#;g"                                                 |
sed -r 's;href="<a href="([^"]*)"[^>]*>.*</a>";href="\1";'          |
sed 's/<table/& class="table table-condensed"/'                     |
sed -zr 's;(<p id="article-info".*</div>)[\t\n ]+(<h1[^<]+</h1>);\2\n\1;'

