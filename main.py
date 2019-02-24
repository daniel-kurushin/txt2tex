#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 18:12:39 2019

@author: dan
"""
from my_sys import argv
from files import loadFile, saveFile
if __name__ == "__main__":
    try:
        inp = argv[1]
        out = argv[2]
        data = loadFile(inp)
        structure = getStructure(data)
        tex = generateTex(structure)
        saveFile(out, tex)
    except Exception as e:
        print("error %s" % e)