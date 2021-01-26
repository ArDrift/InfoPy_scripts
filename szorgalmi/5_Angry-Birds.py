#!/usr/bin/env python3

import turtle
import math

def draw_bg(malacpoz, madarpoz, meret):
  # alaphelyzet, rajzolás közép alulról
  turtle.mode("logo")
  turtle.ht()
  turtle.delay(0)
  turtle.tracer(0)
  turtle.seth(180)
  turtle.up()
  turtle.width(2)
  turtle.fd(80 + 20)
  
  # földfelszín rajzolása
  turtle.seth(90)
  turtle.down()
  turtle.color("black", "#3ea800")
  turtle.begin_fill()
  # alsó téglalap
  turtle.fd(700 // 2)
  turtle.seth(180)
  turtle.fd(10)
  turtle.seth(-90)
  turtle.fd(700)
  turtle.seth(0)
  turtle.fd(10)
  turtle.seth(90)
  turtle.fd(700 // 2)
  turtle.end_fill()
  
  # csúzli rajzolása
  turtle.up()
  turtle.seth(-90)
  turtle.fd(((700 // 2) // 2) - 10)
  turtle.down()
  turtle.color("black", "#a47128")
  turtle.begin_fill()
  turtle.seth(0)
  turtle.fd(60)
  turtle.seth(25)
  turtle.fd(30)
  turtle.seth(-35)
  turtle.fd(5)
  turtle.seth(-145)
  turtle.fd(30 - 5)
  turtle.seth(-35)
  turtle.fd(30 - 5)
  turtle.seth(-145)
  turtle.fd(5)
  turtle.seth(-25 - 180)
  turtle.fd(30)
  turtle.seth(180)
  turtle.fd(60)
  turtle.end_fill()
  
  # malac pillér rajzolása
  turtle.up()
  turtle.seth(90)
  turtle.fd((700 // 2) - 15)
  turtle.seth(0)
  turtle.down()
  turtle.color("black", "#aaaaaa")
  turtle.begin_fill()
  turtle.fd(70)
  turtle.seth(-90)
  turtle.fd(15)
  turtle.seth(0)
  turtle.fd(15)
  turtle.seth(90)
  turtle.fd(15 * 3)
  turtle.seth(180)
  turtle.fd(15)
  turtle.seth(-90)
  turtle.fd(15)
  turtle.seth(180)
  turtle.fd(70)
  turtle.end_fill()
  
  # malac rajzolása
  turtle.up()
  turtle.setpos(malacpoz[0], malacpoz[1] - meret)
  turtle.down()
  turtle.seth(90)
  turtle.color("black", "#6e4")
  turtle.begin_fill()
  turtle.circle(meret, 360, 360)
  #turtle.circle(15, 180 - 15, 360)
  #turtle.seth(turtle.heading() + 90)
  #turtle.fd(3)
  #turtle.seth(90)
  #turtle.circle(3, 360 - 60, 360 - 60)
  #turtle.seth()
  #turtle.fd(10)
  #turtle.seth(-90)
  #turtle.circle(15, 10, 360)
  turtle.end_fill()
  
  # madár rajzolása
  turtle.up()
  turtle.setpos(madarpoz[0], madarpoz[1] - meret)
  turtle.down()
  turtle.color("black", "#b60215")
  turtle.seth(90)
  turtle.begin_fill()
  turtle.circle(meret, 360, 360)
  turtle.end_fill()
  
  return


def shot_input():
  shot_degree = 90 - turtle.numinput("Lövés szög", "Add meg a kilövés szögét:")
  shot_speed = turtle.numinput("Lövés sebesség", "Add meg a lövés sebességét:")

  return shot_degree, shot_speed


def shoot(degree, speed, malacpoz, madarpoz, meret):  

  t = 1
  while (abs(malacpoz[0] - madarpoz[0]) > meret*2 and abs(malacpoz[1] - madarpoz[1]) > meret*2):
    if abs(madarpoz[0]) > 1000 or abs(madarpoz[1]) > 1000:
      return 0
    
    rad = math.radians(degree)
    print("Szög: {:>10.0f}° \nSebesség: {:>5.0f} m/s".format(degree, speed))
    new_v_x = speed * math.cos(rad)
    new_v_y = speed * math.sin(rad) - (10 * t)
    new_v = math.sqrt((new_v_x ** 2) + (new_v_y ** 2))
    
    new_x = speed * t * math.cos(rad)
    new_y = speed * t * math.sin(rad) - ((10 / 2) * (t ** 2)) 
    
    draw_shot(madarpoz[0], madarpoz[1], degree)
    degree = math.degrees(2 * math.pi - math.cos(rad) * (new_v_x / speed))
    #rad = madarpoz[0] * math.tan(rad) - (10 / (2 * (speed ** 2) * (math.cos(rad) ** 2))) * madarpoz[0]**2
    rad = math.radians(degree)
    speed = new_v
    madarpoz[0] += new_x
    madarpoz[1] += new_y
    t += 1
    
  return 1
  
  
def draw_shot(xpoz, ypoz, deg):
  turtle.down()
  turtle.seth(deg)
  turtle.setpos(xpoz, ypoz)
  turtle.dot(10, "red")
  turtle.up()
  return


def main():
  playing = 1

  while playing:
    malac = [168, 0]
    madar = [167 - 400, -40]
    meret = 15
    
    draw_bg(malac, madar, meret)

    shot_val = shot_input()
    if shoot(shot_val[0], shot_val[1], malac, madar, meret):
      print("Nyertél!")
    else:
      print("Ez nem talált!")
    
    playing = turtle.numinput("Új játék?","Szeretnél új játékot? 1 = igen, 0 = nem")
    turtle.clear()
  return


main()
