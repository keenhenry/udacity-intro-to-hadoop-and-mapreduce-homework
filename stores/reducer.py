#!/usr/bin/python

import sys

oldKey = None
numSales, totalSales = 0, 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# Output the total number of records and the sum of all the sales across all the stores

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    numSales += 1
    totalSales += float(thisSale)

print 'Total number of sales is %s and total sales from all the stores is %s' % (str(numSales), str(totalSales),)
