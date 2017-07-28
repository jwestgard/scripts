#!/usr/bin/env python3

import csv
import os
import sys


copybase = '/Volumes/DPI1-3TB/som/'
origbase = '/Volumes/UMary_12943/'

original = {}
copy = {}
basenames = {}
total = 0
verified = 0
errors = 0

with open(sys.argv[1], 'r') as f1:
    reader = csv.DictReader(f1)
    for row in reader:
        fullpath = os.path.join(row['Directory'], row['Filename'])
        filename = fullpath[len(copybase):]
        basename = os.path.basename(filename)
        if basename in basenames.keys():
            basenames[basename].add(filename)
        else:
            basenames[basename] = set([filename])
        checksum = row['MD5']
        copy[filename] = checksum

with open(sys.argv[2], 'r') as f2:
    reader = csv.DictReader(f2)
    for row in reader:
        fullpath = os.path.join(row['Directory'], row['Filename'])
        filename = fullpath[len(origbase):]
        checksum = row['MD5']
        original[filename] = checksum

for filename, checksum in copy.items():
    orig_checksum = original[filename]
    total += 1

    if checksum == orig_checksum:
        print('Verified {0}: {1} = {2}'.format(filename,
                                               checksum, 
                                               orig_checksum
                                               ))
        verified += 1

    else:
        print('ERROR! {0}: {1} != {2}'.format(filename,
                                               checksum,
                                               orig_checksum
                                               ))
        errors += 1

      
print('\nVERIFICATION REPORT')
print('===================')
print('{0} has {1} items'.format(sys.argv[1], len(copy)))
print('{0} has {1} items'.format(sys.argv[2], len(original)))
print('Verified {0}/{1} with {2} errors'.format(verified,total,errors))

print('\nDUPLICATES')
print('==========')
for name, copies in basenames.items():
    if len(basenames[name]) > 1:
        print(name, copies)
