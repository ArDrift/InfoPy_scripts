#!/usr/bin/env python3

import random

def kovezes(hossz, db):
  choice = random.randrange(1, 2+1)
  print("Választás:", choice) 
  if choice == 2 and hossz >= 2:
    db += 1
    return kovezes(hossz - 2, db)
  elif choice == 2 and hossz < 2:
    return kovezes(hossz, db)
  elif choice == 1 and hossz >= 1:
    db += 1
    return kovezes(hossz - 1, db)
  else:
    return db

def main():
  print(kovezes(1, 0))


main()
