#!/bin/bash

for file in "$@";
do
  fileinfo=`ls -sgm "$file"`
  size=`stat -f "%z" "$file"`  
  checksum=`md5 -q "$file"`
  echo -e "$fileinfo \t $size \t $checksum"
done