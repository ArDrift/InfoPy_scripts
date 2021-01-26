#!/usr/bin/env python3

szelesseg = int(input("Mekkora legyen a szélesség?"))
magassag = int(input("Mekkora legyen a magasság?"))

i = 0

print("+", "-" * szelesseg, "+", sep="")

while i < magassag:
    print("|", "." * szelesseg, "|", sep="")
    i += 1

print("+", "-" * szelesseg, "+", sep="")
