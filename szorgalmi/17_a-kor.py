#!/usr/bin/env python3

import pygame
import math
import pygame.gfxdraw

def tav(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def main():
    pygame.init()
    win = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("A kör")

    red = pygame.Color(255, 0, 0)
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    x = 400
    y = 300
    r = 100
    kp = (x, y)
    eps = 10
    font = pygame.font.SysFont("open-sans", 16)
    text = "Középpont: {}, {}, r: {}".format(kp[0], kp[1], r)
    textsf = font.render(text, True, white)

    pygame.gfxdraw.aacircle(win, x, y, r, red)
    win.blit(textsf, (300, 570))
    pygame.display.update()

    event = pygame.event.wait()
    katt = "nem"
    while event.type != pygame.QUIT:
        # egér katt
        if event.type == pygame.MOUSEBUTTONDOWN:
            # középpontra
            if tav(event.pos, kp) <= eps:
                katt = "kp"
            # körívre
            elif abs(tav(event.pos, kp) - r) <= eps:
                katt = "körív"

        elif event.type == pygame.MOUSEMOTION:
            if katt == "kp":
                kp = event.pos
            elif katt == "körív":
                r = int(tav(event.pos, kp))

            if katt != "nem":
                win.fill(black)
                pygame.gfxdraw.aacircle(win, kp[0], kp[1], r, red)
                text = "Középpont: {}, {}, r: {}".format(kp[0], kp[1], r)
                textsf = font.render(text, True, white)
                win.blit(textsf, (300, 570))
                pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONUP:
            katt = "nem"

        event = pygame.event.wait()


main()
