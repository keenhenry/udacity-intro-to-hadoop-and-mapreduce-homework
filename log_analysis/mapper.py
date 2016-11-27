#!/usr/bin/python

# Format of each line is:
# 
# %h %l %u %t \"%r\" %>s %b
#
# where:
#
# %h is the IP address of the client
# %l is identity of the client, or "-" if it's unavailable
# %u is username of the client, or "-" if it's unavailable
# %t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
# %r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol of the request.
# %>s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found). See more information on status codes in W3C.org
# %b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.


import sys
import re

from urlparse import urlparse

p = re.compile(
    '([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)'
)

for line in sys.stdin:
    m = p.match(line)

    if not m:
        continue

    h, l, u, t, r, s, b = m.groups()

    # request string can be further splitted into method, path, query-string and protocol
    try:
        method, url, protocol = r.split()
	parsed_url = urlparse(url)
    except ValueError as e:
	continue  # treated as web log anomaly, skip this line
    print "{0}\t{1}".format(parsed_url.path, s)
