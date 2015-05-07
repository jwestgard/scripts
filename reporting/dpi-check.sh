#!/bin/bash

####################################################################
#      dpi-check.sh    |    Joshua Westgard    |    2014-04-29     #
# ---------------------------------------------------------------- #
# This script searches recursively for image files of a specified  #
# type, and prints the relative path, file size in bytes, and the  #
# x-resolution and y-resolution fields from the exif metadata for  #
# each image.  Execute with: 									   #
#  	   $ ./dpi-check.sh [directory] [*.extension] > output.txt     #
####################################################################

echo -e "PATH\tBYTES\tX-RESOLUTION\tY-RESOLUTION"

for file in $(find $1 -name $2 -type f)
do
  bytes=`stat -f%z "$file"`
  xres=`exiv2 -g Exif.Image.XResolution -Pv "$file"`
  yres=`exiv2 -g Exif.Image.XResolution -Pv "$file"`
  echo -e "$file \t $bytes \t $xres \t $yres" 
done
