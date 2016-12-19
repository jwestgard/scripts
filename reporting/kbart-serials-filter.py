#!/usr/bin/env python3

'''Read CSV export from WorldCat Knowledgebase, filter for patterns matching
   the format of an ISSN in either of two identifier columns, writing lines
   that match the pattern to the output file, and adding ISSNs to a set.
   Report the matched lines, total lines checked, and deduped set of ISSNs.'''
   
import csv
import re
import sys

checked = 0
matches = 0
deduped = set()

# open first argument for reading and get fields
infile = open(sys.argv[1], 'r')
reader = csv.DictReader(infile, delimiter='\t', quoting=csv.QUOTE_NONE)
fieldnames = reader.fieldnames

# open second argument for writing and print header row
outfile = open(sys.argv[2], 'w')
writer = csv.DictWriter(outfile, fieldnames=fieldnames)
writer.writeheader()

# compile regex matching ISSN pattern, ignoring leading/trailing whitespace
issn = re.compile(r'^(\d{4}-\d{4})$')

# for each line of input
for line in reader:
    checked += 1
    print('Matched {0}/{1} lines.'.format(matches, checked), end='\r')
    check1 = line['print_identifier'].strip()
    check2 = line['online_identifier'].strip()
    
    # check the pattern against each identifier column and write matching rows
    if issn.match(check1) or issn.match(check2):
        matches += 1
        writer.writerow(line)
        deduped.update([c for c in [check1, check2] if issn.match(c)])

print('Matched {0}/{1} lines.'.format(matches, checked))
print('Filtering complete! Deduplicating...')
print('{0} unique ISSNs found.'.format(len(deduped)))

for m in sorted(deduped):
    print(m)

infile.close()
outfile.close()
