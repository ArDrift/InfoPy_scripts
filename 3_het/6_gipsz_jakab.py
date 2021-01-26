#!/usr/bin/env python3

eredeti = input("Add meg a nevet: ").split(" ")
forditott = ""

for nev in range(len(eredeti), 0, -1):
  forditott += eredeti[nev - 1]
  if nev != 1:
    forditott += " "
  
print("|" + forditott + "|")
