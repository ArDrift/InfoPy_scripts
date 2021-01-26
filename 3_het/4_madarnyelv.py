#!/usr/bin/env python3

szoveg = input("Add meg a szöveget: ")
madarszoveg = ""
maganhangzok = ["a","á","e","é","o","ó","ö","ő","i","í","u","ú","ü","ű"]

for betu in szoveg:
  if betu in maganhangzok:
    madarszoveg += betu + "v" + betu
  else:
    madarszoveg += betu
    
print("Szöveg madárnyelven:", madarszoveg)
