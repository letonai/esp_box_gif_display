#!/bin/bash
# set -x
FILE="$1"
TMP=$(mktemp -d)
DEST=${FILE[@]::$((${#FILE}-4))}
FPS=$(identify -format "%T\n" $FILE | tail -1)
echo $DEST
magick "$FILE" -coalesce "${TMP}/frame_%05d.jpg"
mkdir -p "${DEST}"
magick convert -resize 320x240! "${TMP}/*" ./"${DEST}"/frame_%05d.jpg

echo "COPY that into your ESP:👇"
echo "${DEST} = ['$DEST',$(ls -l $DEST| wc -l|xargs),$FPS]"