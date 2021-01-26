#!/usr/bin/env python3

def betoltes(file):
  szolista = []
  with open(file, "rt") as f:
    for sor in f:
      szolista.append(sor.rstrip("\n"))
      
  return szolista


def mentes(file, lista):
  with open(file, "wt") as f:
    for elem in lista:
      if elem[0] == "k":
        f.write(elem + "\n")

  return


def main():
  lista = sorted(betoltes("3_szavak_50.txt"))
  mentes("szavak_kbetus.txt", lista)


main()
