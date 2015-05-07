#!/bin/bash
cat $@ |
while read line 
do 
    echo $line
    pid=$line
    echo $pid
done

# url="http://fedora.lib.umd.edu:8080/fedora/get/" $0 "/umd-bdef:umdm/getUMDM/";
# local=$0+".xml";
# curl -o $local $url;