#!/usr/bin/python

import sys

prev_word = None
node_list = []

# Loop around the data
#
# It will be in the format key\tval
# Where key a word, val is the node id's this word appears in
#
# Output the inverted index for each word, including the number of occurrences and the list of node ids it appers in in ascending sorted order

for line in sys.stdin:
    try:
        word, nodes = line.strip().split('\t')
    except ValueError:
        continue

    if prev_word and word != prev_word: # process to a new word
        print '{0} ({1}): {2}'.format(prev_word, len(node_list), ','.join(sorted([node for node in node_list], key=int)))
        del node_list[:]
    node_list.extend(map(lambda s: s.strip('"'), nodes.split(',')))
    prev_word = word

# print last word
print '{0} ({1}): {2}'.format(prev_word, len(node_list), ','.join(sorted(node for node in node_list)))
