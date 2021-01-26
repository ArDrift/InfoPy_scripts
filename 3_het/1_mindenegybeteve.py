#!/usr/bin/env python3

szoveg = input("Add meg a szöveget: ")
egybeszoveg = ""

for betu in szoveg:
  if betu == " ":
    betu = ""
  
  egybeszoveg += betu

print(egybeszoveg)
