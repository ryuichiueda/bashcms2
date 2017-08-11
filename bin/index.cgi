#!/bin/bash -euxv
source "$(dirname $0)/conf"
exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

### VARIABLES ###
tmp=/tmp/$$
dir="$(tr -dc 'a-zA-Z0-9_=' <<< ${QUERY_STRING} | sed 's;=;s/;')"
md="$contentsdir/$dir/main.md"
[ -f "$md" ]

### MAKE MATADATA ###
cat << FIN > $tmp-meta.yaml
---
created_time: $(date -f - < $datadir/$dir/created_time)
modified_time: $(date -f - < $datadir/$dir/modified_time)
title: $(grep '^# ' "$md" | sed 's/^# *//')
---
FIN

### MAKE HTML ###
pandoc --template="$appdir/files/template.html"	\
    -f markdown_github+yaml_metadata_block "$md" "$tmp-meta.yaml"  |
sed -r "/:\/\//!s;<(img src|a href)=\";&/$dir/;"   > $tmp-html 

### OUTPUT ###
sed "1iContent-Type: text/html\n" $tmp-html

rm -f $tmp-*
