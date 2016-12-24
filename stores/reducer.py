#!/usr/bin/python

import sys
from collections import defaultdict

sales_per_weekday = defaultdict(float)
num_sales_per_weekday = defaultdict(int)

# Loop around the data
# It will be in the format key\tval
# Where key is the weekday name, val is the sale amount
#
# Output the average sales for each weekday

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    weekday, cost = data_mapped
    sales_per_weekday[weekday] += float(cost)
    num_sales_per_weekday[weekday] += 1

# print out the results
for day in sales_per_weekday:
    print 'Averate sale for {day}: {sale}'.format(day=day, sale=sales_per_weekday[day]/float(num_sales_per_weekday[day]))
