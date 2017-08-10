#!/bin/bash -euxv
source "$(dirname $0)/conf"
exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

### VARIABLES ###
tmp=/tmp/$$
dir="$(tr -dc 'a-zA-Z0-9_=' <<< ${QUERY_STRING} | sed 's;=;s/;')"
md="$contentsdir/$dir/main.md"
attach="/$dir/"
[ -f "$md" ]

### MAKE HTML ###
pandoc -f markdown_github+yaml_metadata_block "$md" > $tmp-doc

### OUTPUT ###
sed "/DOCUMENT/r $tmp-doc" "$appdir/files/template.html" 	|
sed "s;<img src=\";&$attach;"					|
sed "s;<a href=\";&$attach;"					|
sed "1iContent-Type: text/html\n"

rm -f $tmp-*

