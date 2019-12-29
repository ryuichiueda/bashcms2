#!/bin/bash 
source "$(dirname $0)/../conf"
#exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

echo "Content-Type: text/html"
echo 

echo '<table class="table table-condensed">'

cd $datadir/journals/

find . |
grep journal_                                    |
sort -r                                          |
head                                             |
xargs wc -l                                      |
grep '2.......$'                                 |
sed 's;./journal_....;;'                         |
sed 's;..$;月&日;'                               |
awk '{print $1,$2,NR%2?"odd":"even"}'            |
sed -r 's@(.*) (.*) (.*)@<tr class="\3"><td>\2</td><td>\1</td></tr>@'

echo "</table>" 
