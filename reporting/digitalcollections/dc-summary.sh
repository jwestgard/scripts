#!/bin/bash

#########################################################################
#         dc-summary.sh    |    Joshua Westgard    |    2014-01-26      #
# --------------------------------------------------------------------- #
# This script is designed to aid in the analysis of digital collections #
# by counting the variety of values that are found in specified XML     #
# elements.  Execute with: $ ./dc-summary.sh [myfile.xml]               #
#########################################################################

for file in $@; do

awk 'BEGIN { FS="[<|>]"; print "DIGITAL COLLECTIONS SUMMARY REPORT" }

    /str name="pid"/ {pid=$3}
    
    /geogName type=\"region\"/ {
        for(x=1;x<=NF;x++)if($x~"geogName type=\"region\""){
        h=$(x+1);
        geog[h]+=1;
        }}
        
    /subject type=\"topical\"/ {
        for(x=1;x<=NF;x++)if($x~"subject type=\"topical\""){
        h=$(x+1);
        top[h]+=1
        }}
        
    /subject type=\"temporal\"/ {
        for(x=1;x<=NF;x++)if($x~"subject type=\"temporal\""){
        h=$(x+3);
        temp[h]+=1
        }}
        
    /relationships/ {
        for(x=1;x<=NF;x++)if($x~"relation label=\"archivalcollection\" type=\"isPartOf\""){
        h=$(x+5);
        rel[h]+=1
        }}
        
    END { print "\nGEOGRAPHICAL SUBJECTS:";
        for(hit in geog) {print "\"" hit "\",\"" geog[hit] "\""; geogtot+=geog[hit]};
        print "TOTAL =", geogtot;
        
        print "\nTOPICAL SUBJECTS:";
        for(hit in top) {print "\"" hit "\",\"" top[hit] "\""; toptot+=top[hit]};
        print "TOTAL =", toptot;
        
        print "\nTEMPORAL SUBJECTS:";
        for(hit in temp) {print "\"" hit "\",\"" temp[hit] "\""; temptot+=temp[hit]};
        print "TOTAL =", temptot;
        
        print "\nRELATIONSHIPS";
        for(hit in rel) {print "\"" hit "\",\"" rel[hit] "\""; reltotal+=rel[hit]};
        print "TOTAL =", reltotal;
        }' $file > "${file%.xml}.csv"
done

