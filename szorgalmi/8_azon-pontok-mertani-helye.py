#!/usr/bin/env python3

import pygame
import pygame.gfxdraw
import math

class Pont:
  def __init__(self, x, y):
    self.x = x
    self.y = y


  def __sub__(self, b):
    return Pont(self.x - b.x, self.y - b.y)


  def __abs__(self):
    return math.sqrt(self.x**2 + self.y**2)


def dist_less_eps(dist):
  eps = 5
  return abs(dist) < eps


def main():
  # ablak inicializálása
  pygame.init()
  window = pygame.display.set_mode((640, 480))
  pygame.display.set_caption("Azon pontok mértani helye...")
  
  # konstansok
  red = pygame.Color(255, 0, 0)
  green = pygame.Color(0, 255, 0)
  blue = pygame.Color(0, 0, 255)
  white = pygame.Color(255, 255, 255)
  
  for x in range(0, 640 + 1):
    for y in range(0, 480 + 1):
      # pirosra színezés
      if dist_less_eps(abs(Pont(x, y) - Pont(320, 240)) - 200):
        # kör
        pygame.gfxdraw.pixel(window, x, y, red)

      # zöldre színezés
      if dist_less_eps(abs(Pont(x, y) - Pont(240, 200)) + abs(Pont(x, y) - Pont(400, 280)) - 250):
        # ellipszis
        pygame.gfxdraw.pixel(window, x, y, green)

      # kékre színezés
      if dist_less_eps(abs(abs(Pont(x, y) - Pont(240, 240)) - abs(Pont(x, y) - Pont(400, 240))) - 100):
        # hiperbola
        pygame.gfxdraw.pixel(window, x, y, blue)
        
      # fehérre színezés
      if dist_less_eps(abs(Pont(x, y) - Pont(320, 240)) - abs(Pont(x, y) - Pont(400, y))):
        # parabola
        pygame.gfxdraw.pixel(window, x, y, white)

  pygame.display.update()
  
  quit = False
  while not quit:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
      quit = True

  pygame.quit()


main()
