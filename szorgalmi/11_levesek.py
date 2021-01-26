#!/usr/bin/env python3

class Leves:
  egyfele = 1
  tobbfele = 2
  nincs = 0


def hanyfele_leves(file):
  last_leves = ""
  with open(file, "rt") as f:
    for sor in f:
      if "leves" in sor:
        if last_leves == "":
          last_leves = sor
        elif sor != last_leves:
          return Leves.tobbfele

  if last_leves != "":
    return Leves.egyfele
  else:
    return Leves.nincs


def main():
  kulonfele = hanyfele_leves("11_rendelesek.txt")
  if kulonfele == Leves.egyfele:
    print("Egyféle leves van a rendelések közt.")
  elif kulonfele == Leves.tobbfele:
    print("Többféle leves van a rendelések közt.")
  else:
    print("Nincs leves a rendelések közt.")


main()
