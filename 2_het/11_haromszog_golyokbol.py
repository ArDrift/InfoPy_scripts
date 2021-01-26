#!/usr/bin/env python3

sorszam = int(input("Add meg a háromszög sorainak számát:"))
i = 0

while i < sorszam:
    print(" " * (sorszam - i - 1), end="")
    print("o" * (1 + i * 2), end="\n")
    i += 1
