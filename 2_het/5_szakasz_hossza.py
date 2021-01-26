#!/usr/bin/env python3

import math

print("Szakasz hossza")

koord_a = input("A pont koordinátái (\";\"-vel elválasztva):").split(";")
koord_b = input("B pont koordinátái (\";\"-vel elválasztva):").split(";")

szakasz_hossza = math.sqrt(((float(koord_a[0])) - float(koord_b[0]))**2 + (float(koord_a[1]) - float(koord_b[1]))**2)

print("Az AB szakasz hossza:", szakasz_hossza)
