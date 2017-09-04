#!/bin/env python

area_x = open('./area_x.txt', 'w')
area_y = open('./area_y.txt', 'w')
kind_x = open('./kind_x.txt', 'w')
kind_y = open('./kind_y.txt', 'w')
sig_x = open('./sig_x.txt', 'w')
sig_y = open('./sig_y.txt', 'w')

with open('./data3-x.json') as f:
    all_x = f.readlines()
with open('./data3-y.json') as f:
    all_y = f.readlines()

for i in range(0, len(all_y)):
    x = all_x[i].strip()
    y = all_y[i].strip()

    area = []
    kind = []
    sig = []
    for label in y.split(','):
        if label.startswith('area'):
            area.append(label)
        elif label.startswith('kind') and label != "kind/flake":
            kind.append(label)
        elif label.startswith('sig'):
            sig.append(label)
    if len(area) > 0:
        print>>area_x, x
        print>>area_y, ','.join(area)
    if len(kind) > 0:
        print>>kind_x, x
        print>>kind_y, ','.join(kind)
    if len(sig) > 0:
        print>>sig_x, x
        print>>sig_y, ','.join(sig)



