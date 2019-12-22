#!/bin/bash
source "$(dirname $0)/../conf"
#exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

echo "Content-Type: text/html"
echo 

cat $datadir/journals/journal_$(date "+%Y%m%d") |
wc -l
