#!/usr/bin/env python
# coding: utf-8
from operator import itemgetter
import sys

dict_ip_count = {}
for line in sys.stdin:
    line = line.strip() 
    ip, hour, num = line.split('\t') 
    try:
        if int(start)<=int(hour) and int(hour)<int(end):
                num = int(num)
                dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num
    except ValueError:
        pass
        
sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(1),reverse=True)[0:3]
for ip, count in sorted_dict_ip_count:
    print '%s\t%s' % (ip, count)  
