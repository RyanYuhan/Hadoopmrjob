#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import re

pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    try:
        match = pat.search(line)
        if match:
            print '%s\t%s' % (match.group('hour'), match.group('ip'))
    except:
        pass
