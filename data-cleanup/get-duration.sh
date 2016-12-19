ls  | while read file; do dur=$(ffprobe -show_entries format=duration -i $file | awk -F= '/duration/ {print $2}'); echo $file","$dur; done > ~/Desktop/results.csv
