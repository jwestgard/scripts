#!/bin/bash

##################################################
# ent-convert.sh | Joshua Westgard | 2014-01-26  #
#------------------------------------------------#
# Converts the XML entities for greater than and #
# less than symbols into regular characters.     #
##################################################

for file in $@; do
    sed -i '.bak' 's/&gt;/>/g
                   s/&lt;/</g' $file;
done