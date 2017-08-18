#!/bin/bash -euxv
source "$(dirname $0)/conf"
exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

trap 'rm -f $tmp-*' EXIT

tmp=/tmp/$$

word=$(nkf --url-input <<< ${QUERY_STRING} | sed 's/^word=//' )
numchar=$(nkf -w16B0 <<< "$word" | xxd -plain | tr -d '\n' | sed 's/..../\&#x&;/g')

### 検索 ###
[ -n "$word" ] &&
grep " .*$word" "$datadir/all_markdown" |
awk '{print $1}'                        |
uniq                                    |
tac                                     |
xargs -I@ cat "$datadir/@/link_date"    |
sed 's;$;<br/>;' > $tmp-results

cat << FIN
Content-Type: text/html

<h1>Search</h1>
<input type="text" id="full-search-box" value="" />
<button onclick="fullSearch(document.getElementById('full-search-box').value)" >Search</button>
<br />
FIN

cat $tmp-results
