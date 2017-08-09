#!/bin/bash
dir=$(dirname $0)

echo "Content-Type: text/html"
echo
sed 's/^/\t/' $dir/pages/top/html        |
filehame -lDOCUMENT $dir/template.0.html -
