#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys
# find the date
para = re.compile('\@\@(?P<para1>\d\d*)\-(?P<para2>\d\d*)\@\@')
for l in sys.stdin:
    temp =para.search(l)
para_1 = para.group('para1')
para_2 = para.group('para2')
# iterate the file for mapper
pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    match = pat.search(line)
    if match:
        if match.group('hour') in list(range(int(para_1), int(para_2)+1)):
            print '%s\t%s' % (match.group('ip'), 1)
