#!/usr/bin/python
import re
import sys

para = re.compile('\@\@(?P<para1>\d\d*)\-(?P<para2>\d\d*)\@\@')
pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    try:
        temp = para.search(line)
        if temp:
            para_1 = int(temp.group('para1'))
            para_2 = int(temp.group('para2'))
        match = pat.search(line)
        if match and int(match.group('hour')) >= int(para_1) and int(match.group('hour')) <= int(para_2):
            print '%s\t%s' % (match.group('hour', match.group('ip'))
    except:
        pass
