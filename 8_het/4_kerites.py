#!/usr/bin/env python3

import math

class Pont:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  
  def __str__(self):
    return "{};{}".format(self.x, self.y)
 

def tav(a, b):
  return math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)


def egyenlo(a, b):
  return a.x == b.x and a.y == b.y
  

def beolvas(szoveg):
  pontbe = input("{} (vesszővel (,) elválasztva): ".format(szoveg))
  try:
    koord = Pont(int(pontbe.split(",")[0]), int(pontbe.split(",")[1]))
    return koord
  except:
    print("Kérlek helyesen add meg a koordinátákat (pl. '1, 10')!")


def main():
  kp = beolvas("Kezdőpont")
  keritesh = 0
  ujpont = beolvas("Új pont")
  keritesh += tav(kp, ujpont)
  while not egyenlo(ujpont, kp):
    lastpont = ujpont
    ujpont = beolvas("Új pont")
    keritesh += tav(lastpont, ujpont)
  
  print("A kerítés hossza: {}".format(keritesh)) 


main()
