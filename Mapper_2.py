#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

para = re.compile('\@\@(?P<para1>\d\d*)\-(?P<para2>\d\d*)\@\@')
pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    temp = para.search(line)
    if temp:
        para_1 = temp.group('para1')
        para_2 = temp.group('para2')
    else:
        match = pat.search(line)
        if match and int(match.group('hour')) >= int(para_1) and int(match.group('hour')) <= int(para_2):
            print '%s\t%s' % (match.group('ip'), 1)
