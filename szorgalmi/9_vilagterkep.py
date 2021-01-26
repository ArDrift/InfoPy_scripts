#!/usr/bin/env python3

# A feladat megoldásához felhasználtam: https://docs.python.org/3/library/turtle.html

import turtle

def ttlinit():
  turtle.setup(width=1080, height=540)
  turtle.title("Világtérkép 🌍")
  turtle.delay(0)
  turtle.bgcolor("#8ab5ea")
  turtle.setworldcoordinates(-180, -90, 180, 90)
  turtle.up()
  turtle.ht()


class Pont:
  def __init__(self, x, y):
    self.x = x
    self.y = y


def beolvas(file):
  sokszogek = []
  sokszog = []
  with open(file, "rt") as f:
    for sor in f:
      if sor.rstrip("\n") != "e":
        koord = sor.rstrip("\n").split(" ")
        sokszog.append(Pont(float(koord[0]), float(koord[1])))
      else:
        sokszogek.append(sokszog)
        sokszog = []

  return sokszogek


def drawmap(polylist, pencolor, fillcolor):
  turtle.color(pencolor, fillcolor)
  for sokszog in polylist:
    turtle.begin_fill()
    for pont in sokszog:
      turtle.goto(pont.x, pont.y)
      turtle.down()
    turtle.goto(sokszog[0].x, sokszog[0].y)
    turtle.end_fill()
    turtle.up()


def main():
  ttlinit()
  szigetek = beolvas("9_vilag.txt")
  tavak = beolvas("9_tavak.txt")
  drawmap(szigetek, "#4b1f04", "#efbe61")
  drawmap(tavak, "blue", "#8ab5ea")
  # BME
  turtle.goto(19.05, 47.48)
  turtle.dot(7, "red")

  turtle.done()


main()
