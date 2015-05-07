#!/bin/bash

####################################################################
#      movefiles.sh    |    Joshua Westgard    |    2014-08-15     #
# ---------------------------------------------------------------- #
# Read names of files from the first column of a list of files,    #
# find those files in the specified input directory, and move them #
# to the specified output directory.                               #
#  	   $ ./movefiles.sh [filelist] [indir] [outdir]                #
####################################################################

awk '{ gsub(/"/,""); print $1 }' "$1" | 

while read line; do 
    find "$2" -name "$line" -exec mv {} "$3" \;
done