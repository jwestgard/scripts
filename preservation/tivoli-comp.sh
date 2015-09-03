csvjoin -c "Key" --outer <(cat Archive047_2015-08-07_DPIstats.txt | \
tr -d '"' | \
tr -s [:blank:] ,) filesarchived.txt | \
csvlook
