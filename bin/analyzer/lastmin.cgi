#!/bin/bash
source "$(dirname $0)/../conf"
#exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

min=$(tr -dc '0-9' <<< ${QUERY_STRING})
[ -z "$min" ] && min=30

file_header=$datadir/journals/journal_

echo "Content-Type: text/html"
echo 

FROM=$(date "+%s" -d "$min minutes ago")
TODAY=$(date "+%Y%m%d")
YESTERDAY=(date "+%Y%m%d" -d "1 day ago")
for d in $TODAY $YESTERDAY ; do
	[ -e "$file_header$d" ] && cat "$file_header$d"
done                               |
awk -v f="$FROM" '$3>=f'           |
wc -l
