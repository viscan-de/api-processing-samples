#!/bin/bash

FILE=$(basename $1)
URL="$2$FILE?$3"
echo "$URL"

curl --progress-bar --verbose --request PUT --header "x-ms-blob-type: BlockBlob" --data-binary "@$1" $URL | tee -a "upload.log" ; test ${PIPESTATUS[0]} -eq 0