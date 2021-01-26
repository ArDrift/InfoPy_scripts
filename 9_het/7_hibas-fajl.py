#!/usr/bin/env python3

def beolvas(file):
  pontszamok = []
  with open(file, "rt") as f:
    for sor in f:
      try:
        pontszamok.append(int(sor.rstrip("\n")))
      except ValueError:
        pass

  return pontszamok


def main():
  print(beolvas("7_kzh_pontszam_hibas.txt"))


main()
