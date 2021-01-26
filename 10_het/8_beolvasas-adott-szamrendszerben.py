#!/usr/bin/env python3

# A feladat megoldásához felhasználtam: https://docs.python.org/3/library/stdtypes.html

def tizesbe(rendszer, szamstr):
  res = 0
  for b in range(len(szamstr)):
    if szamstr[b].isdecimal():
      res += int(szamstr[b]) * rendszer ** (len(szamstr) - 1 - b)
    else:
      res += (ord(szamstr[b].upper())-55) * rendszer ** (len(szamstr) - 1 - b)

  return res


def main():
  rendszer = int(input("Add meg a számrendszert: "))
  szam = input("Add meg a számot: ")
  print("A megadott szám 10-es számrendszerben: {}".format(tizesbe(rendszer, szam)))


main()
