#!/usr/bin/env python3

def betolt(file):
  megallok = []
  with open(file, "rt") as f:
    for sor in f:
      megallok.append(sor.rstrip("\n"))
      
  return megallok


def metszi_e(alista, blista):
  for elem in alista:
    if elem in blista:
      return elem

  return None


def main():
  print(metszi_e(betolt("4_m2.txt"), betolt("4_m4.txt")))


main()
