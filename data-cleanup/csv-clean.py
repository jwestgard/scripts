#!/usr/bin/env python3

import csv
import sys

with open(sys.argv[1], 'r') as infile, open(sys.argv[2], 'w') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        if row['TopicalScheme'] is not '':
            row['TopicalScheme'] = 'LCSH'
        writer.writerow(row)
