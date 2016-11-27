#!/usr/bin/python

import sys

prev_ip = None
numHits = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the client ip address, val is the number of hits per ip address
#
# Output the total number of hits per ip address

for line in sys.stdin:

    ip = line.strip()
    if prev_ip and ip != prev_ip: # process to a new ip address
        print '{0}: {1}'.format(prev_ip, numHits)
        numHits = 0
    numHits += 1
    prev_ip = ip

print '{0}: {1}'.format(prev_ip, numHits)
