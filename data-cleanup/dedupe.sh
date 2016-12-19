#!/usr/bin/env bash

ROOTDIR=$1

find $ROOTDIR -type f |
while read file 
do 
	bytes=$(stat "$file" | awk '{print $2}')
	echo -e "$bytes\t$file"
done > filelist.txt

