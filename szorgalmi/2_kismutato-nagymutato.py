#!/usr/bin/env python3

"""
A feladat felkészítéséhez felhasználtam a következő forrást:
https://docs.python.org/3/library/turtle.html
"""

import turtle

ora = int(input("Add meg az órák számát: "))
perc = int(input("Add meg a percek számát: "))
masodperc = int(input("Add meg a másodpercek számát: "))

szinmix = [255, 0, 0]

def print_clock(ora, perc, masodperc):
  # kezdőállás, óra legyen középen
  turtle.speed(0)
  turtle.ht()
  turtle.width(5)
  turtle.up()
  turtle.seth(-90)
  turtle.fd(250)
  turtle.seth(0)
  turtle.down()
  
  # számlap színezés
  turtle.color("#86fc80")
  turtle.begin_fill()
  turtle.circle(250)
  turtle.end_fill()
  turtle.color("#0d83dd")

  for szog in range(0, 360, 6):
    # színek változtatása
    turtle.colormode(255)

    # zöld nő
    if szog in range(0, 60) and szinmix[1] <= 255 - 21:
      szinmix[1] += 21
    # piros csökken
    elif szog in range(60, 120) and szinmix[0] >= 0 + 21:
      szinmix[0] -= 21
    # kék nő
    elif szog in range(120, 180) and szinmix[2] <= 255 - 21:
      szinmix[2] += 21
    # zöld csökken
    elif szog in range(180, 240) and szinmix[1] >= 0 + 21:
      szinmix[1] -= 21
    # piros nő
    elif szog in range(240, 300) and szinmix[0] <= 255 - 21:
      szinmix[0] += 21
    # kék csökken
    elif szog in range(300, 360) and szinmix[2] >= 0 + 21:
      szinmix[2] -= 21

    turtle.color(szinmix)

    # óra, perc strigulák kirajzolása, külső körvonal
    turtle.seth(90 + szog)
    turtle.width(4)
    # óra-strigulák
    if szog % 15 == 0:
      turtle.width(5)
      turtle.fd(20)
      turtle.bk(20)
    # perc-strigulák
    else:
      turtle.fd(10)
      turtle.bk(10)
    turtle.seth(szog)
    turtle.width(5)

    turtle.circle(250, 6)

  # középre helyezés
  turtle.up()
  turtle.setpos(0,0)
  turtle.down()

  # óramutató
  turtle.width(7)
  turtle.color("#720ddd")
  turtle.seth(90 - ora * 30 - perc * 0.5)  
  turtle.fd(120)
  turtle.bk(120)
  
  # percmutató
  turtle.width(5)
  turtle.color("#0d91dd")
  turtle.seth(90 - perc * 6 - masodperc * 0.1)
  turtle.fd(170)
  turtle.bk(170)
  
  # másodpercmutató
  turtle.width(3)
  turtle.color("#dd1e0d")
  turtle.seth(90 - masodperc * 6)
  turtle.fd(220)
  turtle.bk(220)
  
  # középső kör
  turtle.up()
  turtle.seth(-90)
  turtle.fd(10)
  turtle.down()
  turtle.begin_fill()
  turtle.color("#ddbb0d")
  turtle.seth(0)
  turtle.circle(10)
  turtle.end_fill()
  
  turtle.done()

print_clock(ora, perc, masodperc)
