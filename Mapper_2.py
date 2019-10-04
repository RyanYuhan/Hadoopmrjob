#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

par = raw_input('The time you want, the patter is num-num')
par = par.strip()
par = par.split()

pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    match = pat.search(line)
    if match:
        if match.group('hour') in list(range(int(par[0]), int(par[1])+1)):
            print '%s\t%s' % (match.group('ip'), 1)
