#!/usr/bin/env python3
def reset(szam):
  szam = 1
  return szam


def add_one(szam):
  szam += 1
  return szam


def invert(szam):
  return -szam


def times_two(szam):
  return szam * 2


def printmenu():
  print("0. Alapertek visszaallitasa (a = 1)",
        "1. Hozzaad 1-et",
        "2. Megforditja az elojelet",
        "3. Szorozza 2-vel",
        "9. Kilepes", "",
        sep="\n")


def main():
  a = 1
  printmenu()
  try:
    choice = int(input("Válassz menüpontot: "))
  except ValueError:
    print("Kérlek egész számot adj meg!")
    return

  while choice != 9:
    if choice == 0:
      a = reset(a)
    elif choice == 1:
      a = add_one(a)
    elif choice == 2:
      a = invert(a)
    elif choice == 3:
      a = times_two(a)

    print("'a' értéke:", a, "\n")
    printmenu()
    choice = int(input("Válassz menüpontot: "))
  return


main()
