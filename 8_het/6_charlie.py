#!/usr/bin/env python3

class Fagyi:
  def __init__(self, iz, db):
    self.iz = iz
    self.db = db
    

def izkeres(flist, iz):
  for f in range(0, len(flist)):
    if flist[f].iz == iz:
      return f

  return None


def vasarlas(flist):
  try:
    vett = input("Fagyi íze: ")
  except EOFError:
    return
  while vett != "":
    if flist[izkeres(flist, vett)].db >= 1:
      flist[izkeres(flist, vett)].db -= 1
      print("Sikeres vásárlás.")
      if flist[izkeres(flist, vett)].db == 0:
        print("Kifogyott.")
    else:
      print("Nem is volt!")

    try:
      vett = input("Fagyi íze: ")
    except EOFError:
      return


def main():
  fagyilista = [Fagyi("pisztácia", 0), Fagyi("vanília", 3),
  Fagyi("tutti-frutti", 8), Fagyi("karamell", 4), Fagyi("rumos dió", 5),
  Fagyi("kávé", 9)]
  
  vasarlas(fagyilista)


main()
