#!/bin/bash -euxv
source "$(dirname $0)/conf"
exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

### VARIABLES ###
tmp=/tmp/$$
word=$(nkf --url-input <<< ${QUERY_STRING} |
    sed -e 's/key=//' | nkf -w16B0 | xxd -plain |
     sed 's/..../\&#x&;/g' | sed 's/\&#x000a;//g' )


awk -v w="$word" '$2~","w","{print $1}' "$datadir/keywords_list" |
nkf --numchar-input			|
xargs -I@ cat "$datadir/@/link"		|
sed 's/^/* /'				|
sed "1i# Keyword: $word"                |
pandoc --template="$appdir/view/template.html" \
	-f markdown_github+yaml_metadata_block 

