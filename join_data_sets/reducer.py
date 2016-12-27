#!/usr/bin/python

import sys
from collections import defaultdict

prev_user = None
post_dict = defaultdict(str)

for line in sys.stdin:
    fields = line.strip().split('\t')
    user, mark = fields[0], fields[1]

    if prev_user and user != prev_user: # process to a new user
        print '{id}\t{title}\t{tagnames}\t{author_id}\t{node_type}\t{parent_id}\t{abs_parent_id}\t\
               {added_at}\t{score}\t{reputation}\t{gold}\t{silver}\t{bronze}'.format(**post_dict)

    # this implementation does not handle an A with multiple B's correctly; only one B gets printed ...
    if mark == '"A"':
        post_dict['reputation'] = fields[2]
        post_dict['gold'] = fields[3]
        post_dict['silver'] = fields[4]
        post_dict['bronze'] = fields[5]
    elif mark == '"B"':
        post_dict['id'] = fields[2]
        post_dict['title'] = fields[3]
        post_dict['tagnames'] = fields[4]
        post_dict['author_id'] = user
        post_dict['node_type'] = fields[5]
        post_dict['parent_id'] = fields[6]
        post_dict['abs_parent_id'] = fields[7]
        post_dict['added_at'] = fields[8]
        post_dict['score'] = fields[9]

    prev_user = user

# print last record
print '{id}\t{title}\t{tagnames}\t{author_id}\t{node_type}\t{parent_id}\t{abs_parent_id}\t\
       {added_at}\t{score}\t{reputation}\t{gold}\t{silver}\t{bronze}'.format(**post_dict)
