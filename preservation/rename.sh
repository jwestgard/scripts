#!/bin/bash

###########################################################################################
# This shell script finds all .xml files in a specified directory, pipes the found set    #
# to awk, which stores the old path & name, then modifies the active record to end with   #
# the filename [parentdir]-[filename].xml, finally constructing a 'mv' command with the   #
# old path/name and new path/name, and pipes the move command to the shell for execution. #
# EXECUTE WITH ==> $ ./rename.sh [dirname]                                                #
###########################################################################################

find "$@" -name "*.xml" | 
awk 'BEGIN { FS="/"; OFS="/" }
{ old=$0; $NF=$(NF-1)"-"$NF; print "mv " old " " $0 }' | sh