#!/usr/bin/python
import re
import sys

if len(sys.argv) < 3:
    print('Your should input 3 parameters')
if int(sys.argv[1]) < 0 or int(sys.argv[2]) > 17:
    Print('The parameters are out of range')
start_time = sys.argv[1]
end_time = sys.argv[2]
pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    try:
        match = pat.search(line)
        if match and int(match.group('hour')) >= int(start_time) and int(match.group('hour')) <= int(end_time):
            print '%s\t%s' % (match.group('hour'), match.group('ip'))
    except:
        pass
