#!/bin/bash
source "$(dirname $0)/conf"

md="$contentsdir/posts/template/main.md"

echo "Content-Type: text/html"
echo

pandoc -f markdown_github+yaml_metadata_block "$md"
