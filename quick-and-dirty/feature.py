#!/bin/env python

import json
with open('./data.json') as f:
    content = f.readlines()

xf = open('./x.txt', 'w')
yf = open('./y.txt', 'w')

for c in content:
    j = json.loads(c)
    print j
    print>>xf, (j['Title'] + j['Body']).encode('utf-8').replace("\r\n", " ").replace("\n", " ")
    print>>yf, ",".join(j['Labels'])



