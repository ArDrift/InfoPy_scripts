#!/usr/bin/env python3

"""
A feladat elkészítéséhez igénybe vettem az alábbi forrást:
https://docs.python.org/3/library/string.html
"""

bemenet = int(input("Add meg az autó sebességét: "))
autok = [0] * 20

while bemenet:
  for sebesseg in range(10, 200, 10):
    if bemenet in range(sebesseg - 10, sebesseg):
      autok[sebesseg // 10 - 1] += 1
  try:
    bemenet = int(input("Add meg az autó sebességét: "))
  except:
    break

print("km/h", "\t", "\t", "autó")
for sebesseg in range(0, len(autok)):
  print("{:<}-{:<5}".format(sebesseg * 10, sebesseg * 10 + 9), "\t", autok[sebesseg])
