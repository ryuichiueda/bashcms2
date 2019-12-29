#!/bin/bash 
source "$(dirname $0)/../conf"
#exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

echo "Content-Type: text/html"
echo 
echo '<table class="table table-condensed">'

find $datadir/journals/                          |
grep journal_                                    |
xargs wc -l                                      |
grep journals                                    |
sed 's@/.*_@@;s@..$@@'                           |
awk '{a[$2]+=$1}END{for(k in a){print k,a[k]}}'  |
awk '{print $1,$2,NR%2?"odd":"even"}'            |
sed -r 's@(....)(..) (.*) (.*)@<tr class="\4"><td>\1年\2月</td><td>\3</td></tr>@'

echo "</table>" 
