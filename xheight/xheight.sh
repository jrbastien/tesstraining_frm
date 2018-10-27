#!/bin/bash

# This script is based on the tool provided by Nick White
# https://ancientgreekocr.org/
# The whole code can be downloaded with $ git clone http://ancientgreekocr.org/grctraining.git 

rm -f ../langdata/Latin.xheights

while read i ; do
	echo "$i"
	./xheight "$i">>../langdata/Latin.xheights ; \
done <../langdata/frm/frm.fontlist.txt

sed -i -E 's/(\b[A-Za-z_]+)(\s)([A-Za-z_].*)/\1_\3/g' ../langdata/Latin.xheights
sed -i -E 's/(\b[A-Za-z_]+)(\s)([A-Za-z_].*)/\1_\3/g' ../langdata/Latin.xheights
sed -i -E 's/(\b[A-Za-z_]+)(\s)([A-Za-z_].*)/\1_\3/g' ../langdata/Latin.xheights
sed -i -E 's/(\b[A-Za-z_]+)(\s)([A-Za-z_].*)/\1_\3/g' ../langdata/Latin.xheights

