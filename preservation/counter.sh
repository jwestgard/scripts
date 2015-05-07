#!/bin/bash

#################################################
#   counter.sh | Joshua Westgard | 2014-01-25   #
#################################################

awk 'BEGIN {t=0} 
/Total/ {gsub(",", "", $4); t+=$4; print FILENAME "," $4 "," t} 
END {g=t/2^30; print "Total =", t, "bytes or", g, "GB"}' $@