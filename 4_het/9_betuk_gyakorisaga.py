#!/usr/bin/env python3

"""
A feladat elkészítéséhez igénybe vettem az alábbi forrást:
https://docs.python.org/3/library/string.html
"""

szoveg = "TO BE OR NOT TO BE: THAT IS THE QUESTION"
betuk_db = [0] * 26

for betu in range(0, len(szoveg)):
  if szoveg[betu] != " " and szoveg[betu] != ":":
    betuk_db[ord(szoveg[betu]) - 65] += 1

for betu in range(0, len(betuk_db)):
  if betuk_db[betu] != 0:
    print("{}:  {} db,  {:.2%}".format(chr(betu + 65), betuk_db[betu], betuk_db[betu] / sum(betuk_db)))

