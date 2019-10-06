#!/usr/bin/python
from operator import itemgetter
from collections import defaultdict
import sys

dict_ip_count = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    ip, num = line.split('\t')
    try:
        num = int(num)
        dict_ip_count[ip] = dict_ip_count[ip] + num

    except ValueError:
        pass


sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(1), reverse = True)
for ip, count in sorted_dict_ip_count[:3]:
    print ('%s\t%s' % (ip, count))
