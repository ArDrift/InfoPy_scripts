#!/usr/bin/env python3

szo = input("Add meg a titkosítandó szót: ")
titkositott_szo = ""

for betu in szo:
  betu = ord(betu.lower())
  if betu == 122:
    betu = chr(97)
  else:
    betu = chr(betu + 1)
  titkositott_szo += betu
  
print(titkositott_szo)
