#!/usr/bin/env python3
# A3 for COMPSCI220 2015
# Created by Hao CHEN
# UPI: 8476927

import sys

def anagram(data):
    res = dict()
    for s in data:
        key = ''.join(sorted(s))
        try:              
            res[key].append(s)
        except KeyError:
            res[key] = [s]
    out = ('\n'.join(sorted(' '.join(sorted(v)) for v in res.values())))
    print(out)

            
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split('\n')
    for d in data:
        if d != '':
            anagram(d.split(' '))
            print('')