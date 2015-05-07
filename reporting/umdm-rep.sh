#!/bin/bash

#################################################
#  umdm-rep.sh | Joshua Westgard | 2014-01-25   #
#################################################

awk 'BEGIN {print "\nWelcome!\n"}

     /<geogName type="region">/,/<\/geogName>/ {
        if (match($0, ">.*<")){
            geo=substr($0, RSTART+1, RLENGTH-2)}}

     /<subject type="topical">/,/<\/subject>/ {
        while (match($0, ">.*<")){
            print substr($0, RSTART+1, RLENGTH-2)}}

     /<subject type="temporal">/,/<\/subject>/ {
        if (match($0, ">.*<")){
            temp=substr($0, RSTART+1, RLENGTH-2)}}
            
     /<relationships>/,/<\/relationships>/ {
        if (match($0, ">.*<")){
            rel=substr($0, RSTART+1, RLENGTH-2)}}
            
     END {print geo; 
          for(var in top)print var;
          print temp, rel, "Thanks!"}' $@


#  c&&!--c;/<subject type="topical">/{c=2}
#  c&&!--c;/<subject type="temporal">/{c=2}
#  c&&!--c;/<relationships>/{c=3}' 