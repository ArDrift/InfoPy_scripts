#!/usr/bin/env python3

szam = int(input("Melyik számot? "))

while szam != 1:
  for oszto in range(2, szam + 1):
    if szam % oszto == 0:
      print("{}|{}".format(szam, oszto))
      szam = szam // oszto

print("{}|".format(szam))

