#!/usr/bin/env python3

class Vendeg:
  def __init__(self, nev, szobaszam):
    self.nev = nev
    self.szobaszam = int(szobaszam)
  
  
  def __str__(self):
    return "Név: {}, szoba: {}".format(self.nev, self.szobaszam)

 
def emelet(v):
  return v.szobaszam // 100
  
  
def foglalas(vendegek, nev):
  for v in vendegek:
    if v.nev == nev:
      return v

  return None


def szintlista(vendegek):
  szintek = [0] * 8
  for szint in range(0, len(szintek)):
    for vendeg in vendegek:
      if emelet(vendeg) == szint:
        szintek[szint] += 1
  
  return szintek


def legzsufoltabb(vendegek):
  szintlist = szintlista(vendegek)
  for szint in range(0, len(szintlist)):
    if szintlist[szint] == max(szintlist):
      return szint


def main():
  vendeglista = [Vendeg("Dia Dóra", 712), Vendeg("Elektro M Ágnes", 713), Vendeg("Érték Elek", 506)]
  print("Szintlista vendégek száma szerint: {}".format(szintlista(vendeglista)))
  print("A legzsúfoltabb: {}. szint".format(legzsufoltabb(vendeglista)))

main()
