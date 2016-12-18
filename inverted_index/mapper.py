#!/usr/bin/python

"""`mapper`

.tsv file means 'tab separated values' file; so all the fields are separated by tabs.

id, title, tagnames, authorid, body, node_type, parent_id, abs_parentid, added_at, score, state, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line.split('\t')

There are 19 fields in total!

The forum .tsv file contains ^M characters as record delimiter, therefore you will first need to loop through record correctly to parse each record.
"""

import sys
import re
import collections

TOKEN_DELIMITERS = '\W+'

# a dictionary of 'word'-> [list of node ids]
inverse_index = collections.defaultdict(list)

# previous node id
prev_node_id = None

# build inverted index
next(sys.stdin)  # skip first line, because it is the column headers
for line in sys.stdin:

    fields = line.split('\t')
    if len(fields) == 19:  # full record is captured
        nodeid, body = fields[0], fields[4]
        for token in re.split(TOKEN_DELIMITERS, body.strip()):
            inverse_index[token.lower()].append(nodeid)
        prev_node_id = nodeid
    elif len(fields) == 5:  # record not complete, this is the first line of the broken record, continue collecting the rest of the record
        nodeid, body = fields[0], fields[4]
        for token in re.split(TOKEN_DELIMITERS, body.strip()):
            inverse_index[token.lower()].append(nodeid)
        prev_node_id = nodeid
    elif len(fields) == 1:  # record not complete, continue collecting the rest of the record
        for token in re.split(TOKEN_DELIMITERS, fields[0].strip()):
            inverse_index[token.lower()].append(prev_node_id)
    elif len(fields) == 15:  # record completed, this is the last line of the broken record
        for token in re.split(TOKEN_DELIMITERS, fields[0].strip()):
            inverse_index[token.lower()].append(prev_node_id)

# print out index for hadoop streaming
for key, val in inverse_index.iteritems():
    print '{key}\t{val}'.format(key=key, val=','.join(item for item in val))
