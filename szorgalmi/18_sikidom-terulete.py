#!/usr/bin/env python3

import math
import random

def sin_ketx(x, y):
    return y <= math.sin(2 * x)


def par(x, y):
    return y >= 3 * x**2 - 2


def kor(x, y):
    r = 1.5
    kp = (-0.5, 0)
    return (x <= kp[0] + r and x >= kp[0]-r) and (y <= kp[1] + r and y >= kp[1] - r)


def monte_carlo(fvlista, x_r, y_r):
    terulet = abs(x_r[0] - x_r[1]) * abs(y_r[0] - y_r[1])

    bent_db = 0
    kint_db = 0

    for i in range(10000):
        x = random.uniform(x_r[0], x_r[1])
        y = random.uniform(y_r[0], y_r[1])
        bent = 0
        kint = 0
#        print("X: {} Y: {}".format(x, y))
        for f in fvlista:
            if f(x, y):
#                print("Bent: {}".format(f.__name__))
                bent += 1
            else:
#                print("Kint: {}".format(f.__name__))
                kint += 1
        # a pont mindegyiken belül volt
        if bent == len(fvlista):
            bent_db += 1
        else:
            kint_db += 1

    return terulet * (bent_db/(kint_db+bent_db))


def main():
    fv = [par, kor, sin_ketx]
    x_range = (-2, 2)
    y_range = (-2, 2)
    print("Terület: {}".format(monte_carlo(fv, x_range, y_range)))


main()
