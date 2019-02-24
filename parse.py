#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 18:32:21 2019

@author: dan
"""
import re

STRUCTURES = ['part','section', 'subsection']
LEVELS     = ['',r'=(.*)=',r'==(.*)==',r'===(.*)===']
LISTS      = ['-(.*)','#(.*)']
BEGIN      = {
    'LIST': ('begin_list',),
    'ENUM': ('begin_enum',),
}
END        = {
    'LIST': ('end_list',),
    'ENUM': ('end_enum',),
}
ITEM       = 'item'

def getItem(inp, ltype):
    m = re.match(LISTS[ltype], inp)
    if m:
        out = m.group(1).strip()
    else:
        raise ValueError('no match %s %s' % (inp, ltype))
    return (out, ITEM)
    

def getStrName(level):
    return STRUCTURES[level - 1]

def getLevel(inp, level):
    m = re.match(LEVELS[level], inp)
    if m:
        out = m.group(1).strip()
    else:
        raise ValueError('no match %s %s' % (inp, level))
    return (out, getStrName(level))

def getStructure(text_data):
    pars = []
    for par in re.split('\n{2,}', text_data):
        pars += [par]
    print(pars)
    
    stru = []
    in_list = 0
    in_enum = 0
    for par in pars:
        for line in [ _.strip() for _ in par.split('\n') ]:
            if re.match(LEVELS[3], line):
                stru += [getLevel(line, level = 3)]
            elif re.match(LEVELS[2], line):
                stru += [getLevel(line, level = 2)]
            elif re.match(LEVELS[1], line):
                stru += [getLevel(line, level = 1)]
            elif re.match(LISTS[0], line):
                if not in_list:
                    stru += [BEGIN['LIST']]
                    in_list = 1
                stru += [getItem(line, 0)]
            elif re.match(LISTS[1], line):
                if not in_enum:
                    stru += [BEGIN['ENUM']]
                    in_enum = 1
                stru += [getItem(line, 1)]
        if in_list:
            stru += [END['LIST']]
            in_list = 0
        if in_enum:
            stru += [END['ENUM']]
            in_enum = 0
                
    return stru

def generateTex(structure):
    pass

if __name__ == '__main__':
    print(getStructure(
        text_data = """
= Открыт прием заявок на международный конкурс "Чехия_а" =
Прием заявок на Конкурс на лучшие проекты фундаментальных 
научных исследований, проводимый совместно:
- федеральным государственным бюджетным учреждением 
- "Российский фонд фундаментальных исследований" и 
- Чешским научным фондом 

будет осуществляться до 08.04.2019.


= Открыт прием заявок на конкурс "мк" =

Прием заявок на Конкурс на лучшие научные проекты междисциплинарных 
# фундаментальных исследований по теме "Фундаментальные проблемы 
# исследования почв и управление почвенными 
# ресурсами России" (26-905) будет осуществляться до 14.03.2019.

== Открыт прием заявок на конкурс "мк" ==
Прием заявок на Конкурс на лучшие научные 
проекты междисциплинарных фундаментальных 
исследований по теме «Фундаментальные проблемы 
клеточных технологий» (26-904) будет 
осуществляться до 14.03.2019.
        """
    ))