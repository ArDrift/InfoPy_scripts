#!/usr/bin/env python3

import math

print("Tartály festése" + "\n")

magassag = float(input("Milyen magas? "))
sugar = float(input("Mennyi az átmérője? ")) / 2

felulet = 2 * math.pi * sugar * (sugar + magassag) 

dobozok_szama = felulet / 2

print(dobozok_szama, "doboz festék kell.")
