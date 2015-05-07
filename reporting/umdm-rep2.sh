#!/bin/bash

#################################################
#  umdm-rep.sh | Joshua Westgard | 2014-01-25   #
#################################################

awk 'BEGIN {print "\nWelcome!\n"; i=1}    
    /<doc>/,/<\/doc>/ {
        if (match($0, "<str name=\"pid\">.*<\/str>")) pid=substr($0, RSTART+16, RLENGTH-22);
        if (match($0, "<geogName type=\"region\">[^<]*<\/geogName>")) {geog=substr($0, RSTART+24, RLENGTH-35)};
        if (match($0, "<subject type=\"topical\">[^<]*<\/subject>")) {topic=substr($0, RSTART+24, RLENGTH-34)};
        if (match($0, "<subject type=\"temporal\"><decade[^<]*<\/subject>")) {temp=substr($0, RSTART+24, RLENGTH-34)};
        if (match($0, "<relationships>[^<]*<\/relationships>")) {rel=substr($0, RSTART+24, RLENGTH-34)};
        };
        print "\"" pid "\"," "\"" geog "\"," "\"" topic "\"," "\"" temp "\"," "\"" rels
    END {print "Thanks!"}' $@
    
#   /<descMeta/,/<\/title>/ {
#         if (match($0, ">.*<")){
#             title=substr($0, RSTART+1, RLENGTH-2)}}
# 
#      /<geogName type="region">/,/<\/geogName>/ {
#         if (match($0, ">.*<")){
#             i=substr($0, RSTART+1, RLENGTH-2);
#             geo[i]=i}}
# 
#      /<subject type="topical">/,/<\/subject>/ {
#         if (match($0, ">.*<")){
#             i=substr($0, RSTART+1, RLENGTH-2);
#             top[i]=i}}
# 
#      /<subject type="temporal">/,/<\/subject>/ {
#         if (match($0, ">.*<")){
#             i=substr($0, RSTART+1, RLENGTH-2);
#             temp[i]=i}}
#             
#      /<relationships>/,/<\/relationships>/ {
#         if (match($0, ">.*<")){
#             rel=substr($0, RSTART+1, RLENGTH-2)}}        
#      END {
#           print "Result =";
#           print title;
#           for(var in geo) print var;
#           for(var in temp) print var;
#           for(var in top) print var;
#           print rel
#           }' $@
#  c&&!--c;/<subject type="topical">/{c=2}
#  c&&!--c;/<subject type="temporal">/{c=2}
#  c&&!--c;/<relationships>/{c=3}' 