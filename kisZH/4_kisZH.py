#!/usr/bin/env python3

class Datum:
  def __init__(self, honap, nap):
    self.honap = honap
    self.nap = nap


  def __str__(self):
    return "{:>02}.{:>02}".format(self.honap, self.nap)


def elobb_e(a, b):
  if a.honap == b.honap:
    return a.nap < b.nap
  else:
    return a.honap < b.honap


def main():
  datumok = []
  for i in range(2):
    honap = int(input("{}. hónap: ".format(i)))
    nap = int(input("{}. nap: ".format(i)))
    datumok.append(Datum(honap, nap))
    
  if elobb_e(datumok[0], datumok[1]):
    print("{} előbb van, mint {}.".format(datumok[0], datumok[1]))
  elif datumok[0].nap == datumok[1].nap and datumok[0].honap == datumok[1].honap:
    print("A két megadott dátum ugyanaz")
  else:
    print("{} később van, mint {}".format(datumok[0], datumok[1]))


main()
