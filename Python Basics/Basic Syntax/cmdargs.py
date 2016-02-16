#!/usr/bin/env python
import sys

#example of multi-line statements, and raw_input
raw_input \
('press enter key to view information about the command line arguments' \
)

#example of command line arguments usage
print "No. of command line arguments : ", len(sys.argv)
print "List of command line arguments : ", str(sys.argv)
