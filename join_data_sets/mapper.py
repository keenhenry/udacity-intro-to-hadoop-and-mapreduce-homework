#!/usr/bin/python

"""`mapper`
user_ptr_id	reputation	gold	silver	bronze

id	title	tagnames	Xauthor_id	Xbody	node_type	parent_id	abs_parent_id
added_at	score |	state_string	last_edited_id	last_activity_by_id	last_activity_at	active_revision_id
extra	extra_ref_id	extra_count	marked
"""

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    headers = next(reader)
    mark = 'A' if len(headers) == 5 else 'B'
    for line in reader:
        new_line = []
        if mark == 'A':
            new_line.extend([line[0], mark])
            new_line.extend(line[1:])
        elif mark == 'B':
            author_id = line.pop(3)
            line.pop(3)  # remove body field
            new_line.extend([author_id, mark])
            new_line.extend(line[:8])
        writer.writerow(new_line)
mapper()
