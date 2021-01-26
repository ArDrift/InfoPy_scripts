#!/usr/bin/env python3

import re

"""
1.: vicc
2.: ^alma
3.: hely$
4.: ^.nn.$
5.: ^fru...$
6.: ^ó.*ó$
7.: ssz.*ssz.*
8.: (.{4})\1
9.: ^(.{3})\1
10.: ^(.)(.)(.)\3\2\1$
11.: ^(.)(.)(.).\3\2\1$
"""

def main():
  regex = input("Add meg a regexet: ")
  
  with open("5_szavak.txt", "rt", encoding="utf-8") as f:
      for line in f:
          if re.search(regex, line.rstrip("\n")):
              print(line.rstrip("\n"))


main()

