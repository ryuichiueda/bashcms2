#!/bin/bash -euxv
source "$(dirname $0)/conf"
exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

### VARIABLES ###
tmp=/tmp/$$
md="$contentsdir/posts/template/main.md"

### MAKE HTML ###
pandoc -f markdown_github+yaml_metadata_block "$md" > $tmp-doc
sed "/DOCUMENT/r $tmp-doc" "$appdir/files/template.html" > $tmp-html

### OUTPUT ###
sed "1iContent-Type: text/html\n" $tmp-html

rm -f $tmp-*

