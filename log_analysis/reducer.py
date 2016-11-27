#!/usr/bin/python

import sys

prev_path = None
numHits = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# Output the total number of records and the sum of all the sales across all the stores

for line in sys.stdin:

    log_entry = line.strip().split("\t")
    if len(log_entry) != 2:
        # Something has gone wrong. Skip this line.
        continue

    path, status = log_entry

    if path != prev_path: # process to a new page
        print '%s has %s hits' % (prev_path, str(numHits),)
        numHits = 0

    numHits += 1
    prev_path = path

print '%s has %s hits' % (prev_path, str(numHits),)
