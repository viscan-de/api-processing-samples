#!/bin/bash

FILE=$(basename $1)
URL="$2$FILE?$3"
echo "$URL"

curl --request PUT --header "x-ms-blob-type: BlockBlob" --data-binary "@$1" $URL