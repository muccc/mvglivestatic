#!/usr/bin/env python
# -*- coding: latin-1 -*-
#
# "THE BEER-WARE LICENSE" (Revision 42):
# <fpletz@phidev.org> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return.
# updated by vrs 20100305, mate-ware ;-)

import urllib2
import re

# a weng fragil, aber mei
REGEXP = re.compile(r'<tr class="[^"]+">'+
  '<td class="lineColumn">(\w+)</td>'+
  '<td class="stationColumn">([^<]+)<span class="spacer">&nbsp;</span>'+
  '</td><td class="inMinColumn">(\d+)')

s = urllib2.urlopen(
        'http://www.mvg-live.de/ims/dfiStaticAnzeige.svc?haltestelle=Theresienstra%dfe'
        ).read().replace('\r\n', '').replace('\t', '').decode('ISO-8859-1')

d = REGEXP.findall(s)

if len(d) == 0:
    print 'YOU\'RE LOST! \o.O/'
else:
    for (line, dest, t) in d:
        print '%s %-24s %2s' % (line, dest, t)
