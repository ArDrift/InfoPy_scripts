#!/usr/bin/env python3

class Ido:
  def __init__(self, ora, perc):
    while perc >= 60:
      ora += 1
      perc -= 60
    while perc < 0:
      ora -= 1
      perc += 60

    self.ora = ora
    self.perc = perc


def ido_kiir(i):
  return("{:0>2}:{:0>2}".format(i.ora, i.perc))
  

def ido_hozzaad(i, p):
  return Ido(i.ora, i.perc + p)


def ido_eltelt(i1, i2):
  return "{} perc".format((i1.ora - i2.ora) * 60 + i1.perc - i2.perc)   


def ido_kivon(i, p):
  return Ido(i.ora, i.perc - p)


def main():
  proba = Ido(4, 20)
  print(ido_kiir(ido_kivon(proba, -24)))


main()
