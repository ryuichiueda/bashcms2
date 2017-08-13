#!/bin/bash -euxv
source "$(dirname $0)/conf"
exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"
set -o pipefail

trap 'rm $tmp-*' EXIT

### VARIABLES ###
tmp=/tmp/$$
dir="$(tr -dc 'a-zA-Z0-9_=' <<< ${QUERY_STRING} | sed 's;=;s/;')"
[ -z "$dir" ] && dir="pages/top"
md="$contentsdir/$dir/main.md"
[ -f "$md" ]

### MAKE MATADATA ###
cat << FIN | tee /tmp/aho > $tmp-meta.yaml
---
created_time: '$(date -f - < "$datadir/$dir/created_time")'
modified_time: '$(date -f - < "$datadir/$dir/modified_time")'
title: '$(cat "$datadir/$dir/title")'
nav: '$(cat "$datadir/$dir/nav")'
---
FIN

### OUTPUT ###
pandoc --template="$appdir/view/template.html"	\
    -f markdown_github+yaml_metadata_block "$md" "$tmp-meta.yaml"  |
sed -r "/:\/\/|=\"\//!s;<(img src|a href)=\";&/$dir/;"
