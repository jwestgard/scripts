#!/usr/bin/env sh

find $1 -type f -name $2 | 
while read filename
do 
    gs_cmd="($filename) (r) file runpdfbegin pdfpagecount = quit"
    num_pages=$(gs -q -dNODISPLAY -c "$gs_cmd")
    echo $filename $num_pages
done
