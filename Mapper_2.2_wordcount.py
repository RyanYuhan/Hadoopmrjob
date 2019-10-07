#!/usr/bin/env python
import sys
if len(sys.argv) != 2:
    print('You can only print 1 parameter')
    sys.exit()
if len(sys.argv[1]) != 1:
    print('You can just print one letter!')
    sys.exit()
initial = sys.argv[1]
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        if word.startswith(initial):
            print "%s\t%s" % (word, 1)
        else:
            pass
