#!/usr/bin/env python3

import turtle

def beolvas(file):
  pontszamok = []
  with open(file, "rt") as f:
    for sor in f:
      pontszamok.append(int(sor.rstrip("\n")))
      
  return pontszamok


def stat(pontlista):
  dblista = [0] * 11
  for pont in pontlista:
    dblista[pont] += 1
    
  return dblista


def stat_kiir(dblista):
  for i in range(len(dblista)):
    print("{:>2} db {:>2} pontos".format(dblista[i], i))
  
  return "Átment: {} fő, {:.2%}".format(sum(dblista[4:]), sum(dblista[4:]) / sum(dblista))


def diagram(dblista):
  turtle.color("white", "black")
  turtle.ht()
  turtle.delay(0)
  for x in range(len(dblista)):
    turtle.fd(5)
    turtle.seth(90)
    turtle.begin_fill()
    turtle.fd(dblista[x] * 5)
    turtle.seth(0)
    turtle.fd(10)
    turtle.seth(-90)
    turtle.fd(dblista[x] * 5)
    turtle.end_fill()
    turtle.seth(0)
  
  turtle.done()


def main():
  kzh_lista = beolvas("5_kzh_pontszam.txt")
  print(stat_kiir(stat(kzh_lista)))
  diagram(stat(kzh_lista))


main()
