#!/usr/bin/env python3

import turtle

def fraktal(h, n):
  if n == 0:
    turtle.fd(h / 3)
  else:
    fraktal(h / 3, n - 1)
    turtle.left(60)
    fraktal(h / 3, n - 1)
    turtle.right(120)
    fraktal(h / 3, n - 1)
    turtle.left(60)
    fraktal(h / 3, n - 1)


def hopehely(h, n):
  for _ in range(3):
    fraktal(h, n)
    turtle.right(120)


def main():
  hossz = int(input("Hossz: "))
  komplex = int(input("Komplexitás: "))
  turtle.ht()
  turtle.up()
  turtle.goto(-hossz / 3 / 2, 0)
  turtle.down()
  turtle.tracer(0)
  turtle.width(3)
  turtle.color("red")
  hopehely(hossz, komplex)
  turtle.update()
  turtle.done()


main()
