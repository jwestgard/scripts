#!/usr/bin/env python3
from internetarchive import search_items
import sys

# search IA for the first argument
print("Searching IA for {0} ...".format(sys.argv[1]), end=" ")
sys.stdout.flush()
results = search_items(sys.argv[1])

# convert the result to a list of ids
identifiers = [i['identifier'] for i in results]
print("found {0} identifiers.".format(len(identifiers)))

# write the list of ids to the file specified by the 2nd argumentcd
with open(sys.argv[2], 'wt', encoding='utf-8') as outfile:
    print("Writing to file {0} ...".format(sys.argv[2]), end=" ")
    sys.stdout.flush()
    outfile.write('\n'.join(identifiers))
    print("done!")
