#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:00:33 2019

@author: dan
"""

pars = open('/tmp/in').read().split('\n\n')  

npars = []

for par in pars:
    
    npars += [par.replace('\n- ','\n\item; ').replace('\n', ' ')]

print(npars)

out = ""

for par in npars:
    line = ""
    words = par.split()
    n = 0
    l = len(words) - 1
    for word in words:
        if word[ 0] == '"':
            word = word.replace('"', '«')
        else:
            word = word.replace('"', '»')
        if word == '\item;':
            out += line
            line = "\n- "
        else:
            if len(line) < 80:
                line += word + " "
                if n == l:
                    out += line
            else:
                line += word + "\n"
                out += line
                line = ""
        n += 1
    out = out.strip('\n') + "\n\n"
        
out = out.replace('---', '—')
out = out.replace('--', '—')
out = out.replace('\o', '°')
out = out.replace('^2', '²')
out = out.replace('^3', '³')

out = out.replace('1/4','¼')
out = out.replace('1/2','½')
out = out.replace('3/4','¾')
out = out.replace('+/-','±')

open('/tmp/out', 'w').write(out)
