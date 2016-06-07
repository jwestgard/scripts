#!/usr/bin/env bash
# renamer.sh
# renames files matching $1 by replacing $2 with $3

filter=$1
match=$2
replace=$3

for file in $(ls *$filter*);
do
    old=$file
    new=$(echo $file | sed -e "s/$match/$replace/")
    mv $old $new
done
