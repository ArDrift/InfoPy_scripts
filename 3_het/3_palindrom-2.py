#!/usr/bin/env python3

szoveg = input("Add meg a szöveget: ").lower()
egybeszoveg = ""
forditott = ""

for betu in szoveg:
  if betu == " ":
    betu = ""
  
  egybeszoveg += betu

for betu in range(len(egybeszoveg) - 1, -1, -1):
  forditott += egybeszoveg[betu] 

if forditott == egybeszoveg:
  print("A megadott mondat palindróm.")
else:
  print("A megadott mondat nem palindróm.")
