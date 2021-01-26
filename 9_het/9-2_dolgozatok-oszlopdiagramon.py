#!/usr/bin/env python3

import turtle

# A rendezéshez felhasználtam: https://docs.python.org/3/howto/sorting.html#key-functions

class Hallgato:
  def __init__(self, neptun, nev, pont):
    self.neptun = neptun
    self.nev = nev
    self.pont = pont


  def __str__(self):
    return "Név: {}, Neptun: {}, Pont: {}".format(self.nev, self.neptun, self.pont)


def beolvas(file):
  diaklista = []
  with open(file, "rt") as f:
    for sor in f:
      diaklista.append(Hallgato(sor.split(":")[0], sor.split(":")[1], int(sor.split(":")[2])))
      
  return diaklista


def diagram(dolglista):
  turtle.color("white", "black")
  turtle.ht()
  turtle.delay(0)
  for x in range(len(dolglista)):
    turtle.fd(5)
    turtle.seth(90)
    turtle.begin_fill()
    turtle.fd(dolglista[x].pont * 5)
    turtle.seth(0)
    turtle.fd(10)
    turtle.seth(-90)
    turtle.fd(dolglista[x].pont * 5)
    turtle.end_fill()
    turtle.seth(0)
  
  turtle.done()


def main():
  lista1 = beolvas("8_zheredmeny.txt")
  lista2 = list(lista1)
  lista1[0].pont = 27

  lista1 = sorted(lista1, key=lambda hallgato: hallgato.nev)
  lista2 = sorted(lista2, key=lambda hallgato: hallgato.pont)
  for elem in lista2:
    print(elem)
  
  diagram(lista2)


main()
