#!/usr/bin/env python3

import random

alapszoveg = input("Add meg a szöveget: ")
memeszoveg = ""

for karakter in alapszoveg:
  if random.randint(0, 1) == 1:
    karakter = karakter.upper()
  else:
    karakter = karakter.lower()

  memeszoveg += karakter

print(memeszoveg)
