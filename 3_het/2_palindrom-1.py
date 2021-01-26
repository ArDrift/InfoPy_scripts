#!/usr/bin/env python3

szo = input("Add meg a szót: ").lower()

forditott = ""

for betu in range(len(szo) - 1, -1, -1):
  forditott += szo[betu]

if forditott == szo:
  print("A megadott szó palindróm.")
else:
  print("A megadott szó nem palindróm.")
