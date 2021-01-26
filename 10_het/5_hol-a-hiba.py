#!/usr/bin/env python3

# A float számok miatt az egyes ciklusok a kelletüknél többször is lefuthattak, ezért csúszott el a kép bizonyos darabszámoknál. Pl. kerekítéssel megoldható a probléma.

import turtle
 
def negyzet(a):
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.forward(a)
        turtle.left(90)
    turtle.end_fill()
 
def main():
    a = 30  # oldalhossz
    db = int(input("Hány darabból? "))
 
    turtle.speed(0)
    b = 0.0
    while b <= 1.0:
        r = 0.0
        while r <= 1.0:
            turtle.fillcolor(r, 0, b)
            negyzet(a)
            turtle.forward(a)
            r += round(1/(db-1), 2)
        turtle.backward(db*a)
        turtle.left(90)
        turtle.forward(a)
        turtle.right(90)
        b += round(1/(db-1), 2)
 
    turtle.done()


main()
