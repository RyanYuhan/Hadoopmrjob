#!/usr/bin/python

from collections import defaultdict
from operator import itemgetter
import sys
current_hour = None
ipcountdict = defaultdict(int)
for line in sys.stdin:
    hour, ip = line.split('\t')
    if current_hour == hour:
        ipcountdict[ip]+=1
    else:
        sorted_dict_ip_count = sorted(ipcountdict.items(), key=itemgetter(1), reverse = True)
        print ('--------------------')
        print ('The Top 3 IP in '+str(current_hour)+' is')
        for ip, count in sorted_dict_ip_count[:3]:
            print ('%s\t%s' % (ip, count))
        current_hour = hour
        ipcountdict.clear()


if current_hour == hour:
    sorted_dict_ip_count = sorted(ipcountdict.items(), key=itemgetter(1), reverse = True)
    print ('--------------------')
    print ('The Top 3 IP in '+str(current_hour)+' is')
    for ip, count in sorted_dict_ip_count[:3]:
        print ('%s\t%s' % (ip, count))
